import json

import requests
from django.urls import reverse_lazy
from django.views.generic import TemplateView, FormView

from books.forms import MessageForm, ProfileForm
from common.views import TitleMixin


class IndexView(TitleMixin, TemplateView):
    template_name = 'books/index.html'
    title = 'Book Store'


class BooksListView(TitleMixin, TemplateView):
    template_name = 'books/shop.html'
    title = 'Book Store - Products'

    def get(self, request, *args, **kwargs):
        category = kwargs.get('category')
        page = kwargs.get('page')
        self.extra_context = {'category': category}

        if category == 'all':
            if page:
                books = requests.get(f'http://127.0.0.1:8001/api/books/all/?page_number={page}')
            else:
                books = requests.get(f'http://127.0.0.1:8001/api/books/all/')
        else:
            if page:
                books = requests.get(str(f'http://127.0.0.1:8001/api/books/all/?page_number={page}'),
                                     params={'category': category})
            else:
                books = requests.get(f'http://127.0.0.1:8001/api/books/all/', params={'category': category})
        self.extra_context['all_books'] = books.json()
        return super().get(self, request, *args, **kwargs)


class ContactCreateView(TitleMixin, FormView):
    template_name = 'books/contact.html'
    form_class = MessageForm
    success_url = reverse_lazy('books:contact')
    title = 'Book Store - Contact'

    def get(self, request, *args, **kwargs):
        response = requests.get('http://127.0.0.1:8001/api/books/contacts/')
        self.extra_context = {'contacts': response.json()}
        return super().get(self, request, *args, **kwargs)

    def form_valid(self, form):
        requests.post('http://127.0.0.1:8001/api/books/messages/', data=form.cleaned_data)
        return super().form_valid(form)


class ProfileView(TitleMixin, FormView):
    template_name = 'books/profile.html'
    form_class = ProfileForm
    success_url = reverse_lazy('books:profile')
    title = 'Book Store - Profile'
    user_id = None

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        token = self.request.COOKIES.get('Authorization')
        if token:
            req = requests.get('http://127.0.0.1:8000/api/users/login/',
                               headers={'Authorization': f'Token {token}'},
                               params={'token': token})
            context = json.loads(req.text).get('user_data')
            self.user_id = context.get('id')
            kwargs['initial']['first_name'] = context.get('first_name')
            kwargs['initial']['last_name'] = context.get('last_name')
            kwargs['initial']['username'] = context.get('username')
            kwargs['initial']['email'] = context.get('email')
        return kwargs

    def form_valid(self, form):
        requests.patch(f'http://127.0.0.1:8000/api/users/user/{self.user_id}/',
                       headers={'Authorization': f'Token {self.request.COOKIES.get("Authorization")}'},
                       data=form.cleaned_data)
        return super().form_valid(form)


class ReviewDetailView(TitleMixin, TemplateView):
    template_name = 'books/single-product.html'
    title = 'Book Store - Details'

    def get(self, request, *args, **kwargs):
        book_id = kwargs.get('pk')
        if book_id:
            book = requests.get(f'http://127.0.0.1:8001/api/books/all/{book_id}')
            self.extra_context = {'book': book.json()}

        return super().get(self, request, *args, **kwargs)
