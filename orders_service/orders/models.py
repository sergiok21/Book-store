from django.db import models


class Order(models.Model):
    user_id = models.PositiveIntegerField(default=0)
    order_number = models.AutoField(primary_key=True)
    extra_data = models.TextField(blank=True, null=True)

    first_name = models.CharField(max_length=64, blank=True, null=True)
    last_name = models.CharField(max_length=64, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    phone = models.CharField(max_length=64, blank=True, null=True)
    address = models.CharField(max_length=128, blank=True, null=True)
    message = models.TextField(blank=True, null=True)

    total_sum = models.IntegerField(default=0, blank=True, null=True)
    total_quantity = models.IntegerField(default=0, blank=True, null=True)

    created_timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_timestamp']
