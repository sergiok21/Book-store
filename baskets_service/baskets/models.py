from django.db import models


class BasketQuerySet(models.QuerySet):
    def total_sum(self):
        return sum(basket.sum() for basket in self)

    def total_quantity(self):
        return sum(basket.quantity for basket in self)


class Basket(models.Model):
    user_id = models.PositiveIntegerField(default=0)
    product_id = models.PositiveIntegerField(default=0)
    name = models.CharField(max_length=256, unique=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    quantity = models.PositiveSmallIntegerField(default=0)
    message = models.TextField()
    created_timestamp = models.DateTimeField(auto_now_add=True)

    objects = BasketQuerySet.as_manager()
