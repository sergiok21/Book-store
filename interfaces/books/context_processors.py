import json

import requests


def general_recommendations(request):
    context = {}

    previews = requests.get('http://127.0.0.1:8001/api/books/previews/')
    context['previews'] = previews.json().get('results')

    recommendations = requests.get('http://127.0.0.1:8001/api/books/recommendations/')
    context['recommendations'] = recommendations.json().get('results')

    partners = requests.get('http://127.0.0.1:8001/api/books/partners/')
    context['partners'] = partners.json()
    return context


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
    if token:
        req = requests.get('http://127.0.0.1:8000/api/users/login',
                           headers={'Authorization': f'Token {token}'},
                           params={'token': token})
        context = json.loads(req.text).get('user_data')
    return context
