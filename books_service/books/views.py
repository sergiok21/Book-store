from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, CreateView, DetailView

from books.forms import MessageForm
from books.models import Contact, Book
from common.views import TitleMixin


class IndexView(TitleMixin, TemplateView):
    template_name = 'books/index.html'
    title = 'Book Store'


class ContactCreateView(TitleMixin, CreateView):
    model = Contact
    template_name = 'books/contact.html'
    context_object_name = 'contacts'
    form_class = MessageForm
    title = 'Book Store - Contact'
    success_url = reverse_lazy('books:contact')

    def get_queryset(self):
        return Contact.objects.all()

    def form_valid(self, form):
        return super().form_valid(form)


class BooksListView(TitleMixin, ListView):
    model = Book
    template_name = 'books/shop.html'
    context_object_name = 'books'
    title = 'Book Store - Products'
    paginate_by = 6

    def get(self, request, *args, **kwargs):
        category = kwargs.get('category')
        self.extra_context = {'category': category}
        if category == 'all':
            self.queryset = Book.objects.all()
        else:
            self.queryset = Book.objects.filter(category__name__icontains=category)
        return super().get(request, *args, **kwargs)


class ReviewDetailView(TitleMixin, DetailView):
    model = Book
    template_name = 'books/single-product.html'
    context_object_name = 'book'
    title = 'Book Store - Details'
