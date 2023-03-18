from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.views.generic import TemplateView, ListView, CreateView

from books.forms import MessageForm
from books.models import Contact, Message, Book
from common.views import TitleMixin


class IndexView(TitleMixin, TemplateView):
    template_name = 'books/index.html'
    title = 'Book Store'


class ContactCreateView(TitleMixin, CreateView):
    model = Contact
    template_name = 'books/contact.html'
    title = 'Book Store - Contact'
    context_object_name = 'contacts'
    form_class = MessageForm
    success_url = reverse_lazy('books:contact')

    def get_queryset(self):
        return Contact.objects.all()

    def form_valid(self, form):
        return super().form_valid(form)


class BooksListView(TitleMixin, ListView):
    model = Book
    template_name = 'books/shop.html'
    title = 'Book Store - Products'
    context_object_name = 'books'
    paginate_by = 6

    def get(self, request, *args, **kwargs):
        category = kwargs.get('category')
        self.extra_context = {'category': category}
        if category == 'all':
            self.queryset = Book.objects.all()
            return super().get(request, *args, **kwargs)
        else:
            self.queryset = Book.objects.filter(category__name__icontains=category)
            return super().get(request, *args, **kwargs)
