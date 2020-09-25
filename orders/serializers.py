from rest_framework import serializers
from .models import Order, OrderStatus, OrderedItem



class OrderStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderStatus
        fields = ['confirmed', 'pending', 'delivered', 'canceled']

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'

class OrderedItemSerializers(serializers.ModelSerializer):
    class Meta:
        model = OrderedItem
        fields = '__all__'