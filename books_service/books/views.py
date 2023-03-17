from django.views.generic import TemplateView

from common.views import TitleMixin


class IndexView(TitleMixin, TemplateView):
    template_name = ''
    title = 'Book Store'
