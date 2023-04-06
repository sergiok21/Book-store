import json

from rest_framework import serializers

from .models import Order


class OrderSerializer(serializers.ModelSerializer):
    extra_data = serializers.SerializerMethodField()

    class Meta:
        model = Order
        fields = ['order_number', 'first_name', 'last_name', 'email', 'phone', 'address', 'message',
                  'total_sum', 'total_quantity', 'created_timestamp', 'extra_data']
        read_only_fields = ['extra_data', 'created_timestamp']

    def get_extra_data(self, obj):
        return json.loads(obj.extra_data)
