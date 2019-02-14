from django.db import models

class Restaurant(models.Model):
    name = models.CharField(max_length = 200)
    owner_name = models.CharField(max_length=100)
    email = models.EmailField(max_length = 200)
    phone_no = models.IntegerField(max_length = 10)
    gst = models.IntegerField(max_length=15)
    address = models.CharField(max_length = 300)
    city = models.CharField(max_length = 20)
    district = models.CharField(max_length = 50)
    place = models.CharField(max_length = 20)
    pincode = models.IntegerField(max_length = 6)
