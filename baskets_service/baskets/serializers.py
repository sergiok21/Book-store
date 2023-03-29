from rest_framework import serializers

from .models import Basket


class BasketSerializer(serializers.ModelSerializer):
    book_id = serializers.IntegerField()

    class Meta:
        model = Basket
        fields = [
            'id', 'book_id', 'name', 'price', 'quantity', 'image', 'sum', 'created_timestamp'
        ]
        read_only_fields = ['name', 'price', 'quantity', 'image', 'created_timestamp', 'sum']


class TotalBasketSerializer(serializers.ModelSerializer):
    total_sum = serializers.SerializerMethodField()
    total_quantity = serializers.SerializerMethodField()

    class Meta:
        model = Basket
        fields = [
            'total_sum', 'total_quantity'
        ]
