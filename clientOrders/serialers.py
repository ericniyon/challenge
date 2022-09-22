from rest_framework import serializers
from .models import ClientOrders


class CreateOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClientOrders
        fields = ['id', 'orderName']


class UserOrderListSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClientOrders
        fields = ['id', 'orderName']