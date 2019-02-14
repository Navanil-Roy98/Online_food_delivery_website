from django.db import models
from django.db.models.fields import IntegerField, TextField

from restaurant.models import Restaurant


class Dishes(models.Model):
    r_id = models.ForeignKey(Restaurant,on_delete='DO_NOTHING')
    dish_name = models.TextField()
    price =  models.IntegerField()
    veg = models.BooleanField()

