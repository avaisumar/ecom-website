from django.db import models


# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=200)
    price = models.FloatField()
    discount_price = models.CharField(max_length=200)
    category = models.CharField(max_length=200)
    description = models.TextField()
    image = models.CharField(max_length=300)


class Order(models.Model):
    items = models.CharField(max_length=1000, default="")
    name = models.CharField(max_length=200, default="")
    email = models.CharField(max_length=200, default="")
    address = models.CharField(max_length=1000, default="")
    city = models.CharField(max_length=200, default="")
    state = models.CharField(max_length=200, default="")
    zipcode = models.CharField(max_length=200, default="")
    total=models.CharField(max_length=200,default="")
