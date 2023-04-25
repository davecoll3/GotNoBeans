from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class Category(models.Model):
    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Product(models.Model):
    category = models.ForeignKey(
        'Category', null=True, blank=True, on_delete=models.SET_NULL
    )
    sku = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    description = models.TextField()
    rating = models.DecimalField(
        max_digits=6, decimal_places=1, null=True, blank=True
    )
    yield_in_cups = models.PositiveIntegerField(
        validators=[
            MaxValueValidator(10),
            MinValueValidator(1)
        ],
        null=True,
        blank=True,
    )
    material = models.CharField(max_length=50, null=True, blank=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name
