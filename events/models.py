from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

from products.models import Product


def validate_date(date):
    if date < timezone.now().date():
        raise ValidationError("Event date cannot be in the past")


class Event(models.Model):

    name = models.CharField(max_length=100)
    date = models.DateField(default=timezone.now, validators=[validate_date])
    time = models.TimeField(default='12:00')
    location = models.CharField(max_length=100)
    description = models.TextField()
    street_address = models.CharField(max_length=80, null=True, blank=True)
    town_or_city = models.CharField(max_length=40)
    postcode = models.CharField(max_length=8)
    products = models.ManyToManyField(Product, blank=True)

    class Meta:
        unique_together = ["name", "date", "time", "location", "town_or_city"]

    def __str__(self):
        return self.name
