from django.urls import reverse, reverse_lazy
from django.views.generic import TemplateView, ListView, CreateView

from books.forms import MessageForm
from books.models import Contact, Message
from common.views import TitleMixin


class IndexView(TitleMixin, TemplateView):
    template_name = 'books/index.html'
    title = 'Book Store'


class ContactListView(TitleMixin, CreateView):
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
