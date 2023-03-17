from books.models import Preview, Recommendation


def general_recommendations(request):
    return {'previews': Preview.objects.all(), 'recommendations': Recommendation.objects.all()}
