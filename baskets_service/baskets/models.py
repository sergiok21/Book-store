import json

import requests
from django.db import models
from rest_framework import status


class BasketQuerySet(models.QuerySet):
    def total_sum(self):
        return sum(basket.sum() for basket in self)

    def total_quantity(self):
        return sum(basket.quantity for basket in self)


class Basket(models.Model):
    user_id = models.PositiveIntegerField(default=0)
    book_id = models.PositiveIntegerField(default=0)
    name = models.CharField(max_length=256, blank=True, null=True)
    price = models.DecimalField(max_digits=6, decimal_places=2, default=0)
    quantity = models.PositiveSmallIntegerField(default=0)
    image = models.URLField(max_length=512, blank=True, null=True)
    message = models.TextField(blank=True, null=True)
    created_timestamp = models.DateTimeField(auto_now_add=True)

    objects = BasketQuerySet.as_manager()

    @classmethod
    def create_or_update(cls, user_id, book_id, message):
        baskets = Basket.objects.filter(user_id=user_id, book_id=book_id)

        if not baskets.exists():
            response = requests.get(f'http://127.0.0.1:8001/api/books/all/{book_id}/')
            if response.status_code == status.HTTP_200_OK:
                data = json.loads(response.text)
                name = data.get('name')
                price = data.get('price')
                image = data.get('image')
                obj = Basket.objects.create(
                    user_id=user_id, book_id=book_id, name=name, price=price, image=image, quantity=1, message=message
                )
                is_created = True
                return obj, is_created
        else:
            basket = baskets.first()
            basket.quantity += 1
            basket.save()
            is_created = False
            return basket, is_created

    def sum(self):
        return self.price * self.quantity
