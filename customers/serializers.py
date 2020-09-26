from rest_framework import serializers
from .models import CustomerCart, CustomerCartItem


class CustomerCartSerializer(serializers.ModelSerializer):
    class Meta:
      model = CustomerCart
      fields = '__all__'

class CustomerCartItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomerCartItem
        fields = '__all__'

