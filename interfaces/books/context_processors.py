import json

import requests


def books_info(request):
    context = {}

    categories = requests.get('http://127.0.0.1:8001/api/books/categories/')
    context['categories'] = categories.json()

    books = requests.get('http://127.0.0.1:8001/api/books/all/2/')
    context['books'] = books.json()

    return context


def user_info(request):
    context = {'username': None}
    token = request.COOKIES.get('Authorization')
    user = request.COOKIES.get('User')
    if token:
        header = {'Authorization': f'Token {token}'}
        cookies = {'User': user}
        login = requests.get('http://127.0.0.1:8000/api/users/login/', headers=header)
        basket = requests.get('http://127.0.0.1:8003/api/baskets/total/',
                              headers=header, cookies=cookies)
        context = json.loads(login.text).get('user_data')
        context['basket_info'] = json.loads(basket.text)
    return context
