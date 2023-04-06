import json
import requests
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView, FormView
from rest_framework import status

from baskets.forms import CheckoutForm
from common.views import TitleMixin


class BasketListView(TitleMixin, TemplateView):
    template_name = 'baskets/basket.html'
    title = 'Book Store - Basket'

    def get(self, request, *args, **kwargs):
        token = request.COOKIES.get('Authorization')
        user_id = request.COOKIES.get('User')
        if token and user_id:
            headers = {'Authorization': f'Token {token}'}
            cookies = {'User': user_id}
            response = requests.get('http://127.0.0.1:8003/api/baskets/current/',
                                    headers=headers, cookies=cookies)
            if response.status_code == status.HTTP_200_OK:
                self.extra_context = {'baskets': json.loads(response.text)}
            else:
                return HttpResponseRedirect(request.META['HTTP_REFERER'])
        else:
            return HttpResponseRedirect(request.META['HTTP_REFERER'])
        return super().get(request, *args, **kwargs)


class BasketFormView(TitleMixin, FormView):
    template_name = 'baskets/checkout.html'
    form_class = CheckoutForm
    success_url = reverse_lazy('baskets:success')
    title = 'Book Store - Checkout'

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        token = self.request.COOKIES.get('Authorization')
        if token:
            req = requests.get('http://127.0.0.1:8000/api/users/login/',
                               headers={'Authorization': f'Token {token}'},
                               params={'token': token})
            context = json.loads(req.text).get('user_data')
            kwargs['initial']['first_name'] = context.get('first_name')
            kwargs['initial']['last_name'] = context.get('last_name')
            kwargs['initial']['email'] = context.get('email')
        return kwargs

    def form_valid(self, form):
        token = self.request.COOKIES.get('Authorization')
        user_id = self.request.COOKIES.get('User')

        headers = {'Authorization': f'Token {token}'}
        cookies = {'User': user_id}

        get_basket = requests.get('http://127.0.0.1:8003/api/baskets/current/',
                                  headers=headers, cookies=cookies)
        get_total = requests.get('http://127.0.0.1:8003/api/baskets/total/',
                                 headers=headers, cookies=cookies)
        result = {'extra_data': get_basket.text}
        result.update(form.cleaned_data)
        result.update(**json.loads(get_total.text))

        send_order = requests.post('http://127.0.0.1:8004/api/orders/current/',
                                   headers=headers, cookies=cookies, data=result)

        if send_order.status_code == status.HTTP_201_CREATED:
            requests.delete('http://127.0.0.1:8003/api/baskets/current/delete/',
                            headers=headers, cookies=cookies)
            return super().form_valid(form)
        else:
            return HttpResponseRedirect(self.request.META['HTTP_REFERER'])


class SuccessTemplateView(TitleMixin, TemplateView):
    template_name = 'baskets/success.html'
    title = 'Book Store - Checkout Success'


def add_to_basket(request, book_id):
    token = request.COOKIES.get('Authorization')
    user = request.COOKIES.get('User')
    requests.post('http://127.0.0.1:8003/api/baskets/current/',
                  headers={'Authorization': f'Token {token}'},
                  data={'book_id': book_id, 'user_id': user})
    return HttpResponseRedirect(request.META['HTTP_REFERER'])


def remove_from_basket(request, book_id):
    token = request.COOKIES.get('Authorization')
    user = request.COOKIES.get('User')
    requests.delete(f'http://127.0.0.1:8003/api/baskets/current/{book_id}/',
                    headers={'Authorization': f'Token {token}'},
                    cookies={'User': user})
    return HttpResponseRedirect(request.META['HTTP_REFERER'])
