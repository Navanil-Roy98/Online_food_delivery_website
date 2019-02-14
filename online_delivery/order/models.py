from django.db import models

from restaurant.models import Restaurant
from customer.models import Customer

class Order(models.Model):
    r_id = models.ForeignKey(Restaurant,on_delete='DO_NOTHING')
    c_id = models.ForeignKey(Customer,on_delete='DO_NOTHING')
    bill_amount = models.IntegerField()
    address = models.TextField()
    city = models.CharField(max_length = 50)
    pincode = models.IntegerField(max_length=6)
