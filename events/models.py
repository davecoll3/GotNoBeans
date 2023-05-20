from django.db import models
from django.contrib.auth.models import User

from products.models import Product


class Event(models.Model):

    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    name = models.CharField(max_length=100)
    date = models.DateField()
    time = models.TimeField(null=True, blank=True)
    location = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    street_address = models.CharField(max_length=80, null=True, blank=True)
    town_or_city = models.CharField(max_length=40)
    postcode = models.CharField(max_length=8, null=True, blank=True)
    products = models.ManyToManyField(Product, blank=True)

    def __str__(self):
        return self.name
