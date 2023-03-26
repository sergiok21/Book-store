from rest_framework import serializers

from .models import Book, BookCategory, Preview, Recommendation, Partner, Contact, Message


class BookSerializer(serializers.ModelSerializer):
    category = serializers.SlugRelatedField(slug_field='name', queryset=BookCategory.objects.all())

    class Meta:
        model = Book
        fields = [
            'id', 'name', 'description', 'price', 'quantity', 'image', 'category'
        ]


class BookCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = BookCategory
        fields = [
            'id', 'name', 'description'
        ]


class PreviewSerializer(serializers.ModelSerializer):
    book = serializers.SlugRelatedField(slug_field='id', queryset=Book.objects.all())

    class Meta:
        model = Preview
        fields = [
            'id', 'book', 'name', 'description', 'image'
        ]


class RecommendationSerializer(serializers.ModelSerializer):
    book = serializers.SlugRelatedField(slug_field='id', queryset=Book.objects.all())

    class Meta:
        model = Recommendation
        fields = [
            'id', 'book', 'name', 'description', 'price', 'image'
        ]


class PartnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Partner
        fields = [
            'id', 'name', 'image'
        ]


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = [
            'id', 'email', 'phone', 'country', 'city',
            'street', 'house', 'corps', 'postal'
        ]


class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = [
            'id', 'name', 'email', 'message'
        ]
