from rest_framework import serializers
from .models import Shop, Products, Category, CustomerList, Domain
from users.serializers import UserSerializer



class ShopSerializer(serializers.ModelSerializer):
    name = serializers.CharField()
    class Meta:
        model = Shop
        fields = '__all__'

    def validate_name(self, value):
        shop = Shop.objects.filter(name=value)
        if shop:
          raise serializers.ValidationError('Store name already exists')

   
class DomainSerializer(serializers.ModelSerializer):
    class Meta:
      model = Domain
      fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = '__all__'



class CustomerListSerializer(serializers.ModelSerializer):
    class Meta:
      model = CustomerList
      fields = '__all__'


