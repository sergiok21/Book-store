from books.models import Preview, Recommendation, Book, BookCategory, Partner


def general_recommendations(request):
    return {'previews': Preview.objects.all(),
            'recommendations': Recommendation.objects.all(),
            'partners': Partner.objects.all()
            }


def books_info(request):
    return {'books': Book.objects.all(), 'categories': BookCategory.objects.all()}
