from django.db import models
from django.contrib.auth import get_user_model
from cloudinary.models import CloudinaryField

# Create your models here.

class Shop(models.Model):
    name = models.CharField(max_length=100)
    buisness_type = models.CharField(max_length=20)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class CustomerList(models.Model):
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

class Category(models.Model):
    category_name = models.CharField(max_length=50)

    def __str__(self):
        return self.category_name

class Products(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    description = models.CharField(max_length=255)
    price = models.IntegerField()
    quantity = models.IntegerField()
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Images(models.Model):
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    image = CloudinaryField('image')

    def __str__(self):
        return self.product.name
