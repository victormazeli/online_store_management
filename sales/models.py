from django.db import models

# Create your models here.

class Transaction(object):
    currency = models.CharField(max_length= 10)
    amount = models.FloatField(blank=True, null=True, default=0.00)
    status = models.CharField(max_length= 10)
    txn_date = models.DateTimeField(auto_now_add=True)
    ref = models.CharField(max_length= 256)
    cutomer_id = models.CharField(max_length= 256)
    cutomer_f_name = models.CharField(max_length= 256)
    cutomer_l_name = models.CharField(max_length= 256)
    customer_email = models.EmailField()
    # shop_name = models.CharField(max_length=100)
    
    class Meta:
        ordering = ['txn_date']   


# class sales(models.Model):
#     amount = models.FloatField(default=0.00)
#     date = models.DateField(auto_now_add=True)

#     class Meta:
#         ordering = ['date']  