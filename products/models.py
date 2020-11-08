from django.db import models

# Create your models here.

UNIT_CHOICE = (
    ("kg", "kg"),
    ("cm", "cm"),
    ("pcs", "pcs"),
    ("boxes", "boxes"),
)


class Products(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=255)
    price = models.FloatField(default=0.00)
    discounted_price = models.FloatField(default=0.00)
    quantity_in_stock = models.IntegerField(default=0)
    unit = models.CharField(max_length=20, default='pcs', choices=UNIT_CHOICE)
    sales = models.IntegerField(default=0)
    extra_detail = models.CharField(max_length=255, blank=True, null=True)
    in_stock = models.BooleanField(default=False)

    def __str__(self):
        return self.name
    

class ProductImages(models.Model):
    product = models.OneToOneField(Products, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='product_images')


class ProductOption(models.Model):
    product = models.OneToOneField(Products, on_delete=models.CASCADE)
    name = models.CharField(max_length=120)
   
   
class ProductVariation(models.Model):
    option = models.ForeignKey(ProductOption, on_delete=models.CASCADE)
    value = models.CharField(max_length=50)
    price = models.FloatField(default=0.00)
    quantity = models.IntegerField(default=0)

    def __str__(self):
        return self.option.option