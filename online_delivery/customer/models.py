from django.db import models

class Customer(models.Model):
    name = models.CharField(max_length = 200)
    email = models.EmailField(max_length = 200)
    phone_no = models.IntegerField()


