import datetime
import json
import requests
from django.shortcuts import redirect
from django.urls import reverse
from django.views.generic import TemplateView
from rest_framework import status

from common.views import TitleMixin


class OrdersTemplateView(TitleMixin, TemplateView):
    template_name = 'orders/orders.html'

    def get(self, request, *args, **kwargs):
        token = request.COOKIES.get('Authorization')
        user_id = request.COOKIES.get('User')
        if token and user_id:
            headers = {'Authorization': f'Token {token}'}
            cookies = {'User': user_id}
            response = requests.get('http://127.0.0.1:8004/api/orders/current/',
                                    headers=headers, cookies=cookies)
            if response.status_code == status.HTTP_200_OK:
                self.extra_context = {'orders': json.loads(response.text)}
            else:
                return redirect(reverse('books:index'))
        else:
            return redirect(reverse('books:index'))
        return super().get(request, *args, **kwargs)


class CurrentOrderTemplateView(TitleMixin, TemplateView):
    template_name = 'orders/current-order.html'

    def get(self, request, *args, **kwargs):
        token = request.COOKIES.get('Authorization')
        user_id = request.COOKIES.get('User')
        if token and user_id:
            headers = {'Authorization': f'Token {token}'}
            cookies = {'User': user_id}
            order_id = kwargs.get('pk')
            response = requests.get(f'http://127.0.0.1:8004/api/orders/current/{order_id}/',
                                    headers=headers, cookies=cookies)
            if response.status_code == status.HTTP_200_OK:
                self.extra_context = {'order': json.loads(response.text)}

                date_string = self.extra_context['order']['created_timestamp']
                date = datetime.datetime.strptime(date_string, "%Y-%m-%dT%H:%M:%S.%fZ")
                self.extra_context['order']['created_timestamp'] = date
            else:
                return redirect(reverse('books:index'))
        else:
            return redirect(reverse('books:index'))
        return super().get(request, *args, **kwargs)
