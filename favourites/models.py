from django.db import models
from django.contrib.auth.models import User

from products.models import Product


class Favourites(models.Model):

    class Meta:
        verbose_name_plural = 'Favourites'

    # Creates a one-to-one relationship with user
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # Creates a many-to-many relationship with Product model
    products = models.ManyToManyField(Product)

    def __str__(self):
        return f"{self.user}'s favourites"
