from books.models import Preview, Recommendation, Book, BookCategory, Partner


def general_recommendations(request):
    return {
        'previews': Preview.objects.all(),
        'recommendations': Recommendation.objects.all(),
        'partners': Partner.objects.all()
    }


def books_info(request):
    return {'books': Book.objects.all(), 'categories': BookCategory.objects.all()}


def get_user_info(request):
    token = request.COOKIES.get('Authorization', None)
    if token:
        return {'token': token}
    else:
        return {'token': []}
