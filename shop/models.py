from django.db import models
from django.contrib.auth import get_user_model


# Create your models here.

class Shop(models.Model):
    name = models.CharField(max_length=100)
    buisness_type = models.CharField(max_length=20)
    phone_no = models.IntegerField(null=True, blank=True)
    address = models.CharField(max_length=256, null=True, blank=True)
    state = models.CharField(max_length=256, null=True, blank=True)
    city = models.CharField(max_length=256, null=True, blank=True)
    site_url = models.URLField(null=True, blank=True)
    logo = model.ImageField(upload_to='/profile_pic', null=True, blank=True)
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
    users = models.ManyToManyField(get_user_model(), through='Order', blank=True)
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    description = models.CharField(max_length=255)
    price = models.IntegerField()
    quantity = models.IntegerField()
    image = models.ImageField(upload_to='product_images/', null=True, blank=True)
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

# class Images(models.Model):
#     product = models.ForeignKey(Products, on_delete=models.CASCADE)
#     image = CloudinaryField('image')

#     def __str__(self):
#         return self.product.name
