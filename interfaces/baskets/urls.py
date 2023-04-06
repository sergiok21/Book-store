from django.urls import path

from baskets.views import add_to_basket, remove_from_basket, BasketListView, BasketFormView, SuccessTemplateView

app_name = 'baskets'

urlpatterns = [
    path('current/', BasketListView.as_view(), name='basket'),
    path('current/checkout/', BasketFormView.as_view(), name='checkout'),
    path('current/checkout/success', SuccessTemplateView.as_view(), name='success'),
    path('add-<int:book_id>/', add_to_basket, name='add'),
    path('remove-<int:book_id>/', remove_from_basket, name='remove'),
]
