from rest_framework import serializers
from shop.models import Shop
from .models import CustomUser



class ShopSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shop
        fields = '__all__'

    # def validate_name(self, value):
    #     shop = Shop.objects.filter(name=value)
    #     if shop:
    #       raise serializers.ValidationError('Store name already exists')




class UserSerializer(serializers.ModelSerializer):
    class Meta:
      model = CustomUser
      fields = '__all__'


