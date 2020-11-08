from django.db import models
from customers.models import CustomerCart, Customers
# Create your models here.

    
ORDER_STATUS_CHOICE = (
    ("paid", "paid"),
    ("unpaid", "unpaid"),
    ("open", "open"),
    ("cancelled", "cancelled"),
)
    
class Order(models.Model):
    order_id = models.CharField(max_length=126, blank=True)
    cart = models.ForeignKey(CustomerCart, on_delete=models.CASCADE)
    status = models.CharField(default='open', choices=ORDER_STATUS_CHOICE, max_length=126)
    customer_details = models.ForeignKey(Customers, on_delete=models.CASCADE)
    shipping_cost = models.FloatField(default=0.00)
    total_cost = models.FloatField(default=0.00)
    date_created = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.order_id
    
    class Meta:
        ordering = ['date_created']
