from django.db import models

from customer.models import Customer
from order.models import Order
from restaurant.models import Restaurant

class Order_details(models.Model):
    r_id = models.ForeignKey(Restaurant,on_delete='DO_NOTHING')
    c_id = models.ForeignKey(Customer,on_delete='DO_NOTHING')
    o_id = models.ForeignKey(Order,on_delete='DO_NOTHING')
    qty = models.IntegerField()
    price = models.IntegerField()                       # price per item
