from django.db import models


from django.core.validators import MaxValueValidator, MinValueValidator

from products.models import Product


class Recipe(models.Model):

    class Meta:
        verbose_name_plural = 'Recipes'

    ex_course = 'Extra-Coarse'
    coarse = 'Coarse'
    medium = 'Medium'
    m_fine = 'Medium-Fine'
    fine = 'Fine'
    s_fine = 'Superfine'

    GRIND = [
        (ex_course, 'Extra-Coarse'),
        (coarse, 'Coarse'),
        (medium, 'Medium'),
        (m_fine, 'Medium-Fine'),
        (fine, 'Fine'),
        (s_fine, 'Superfine'),
    ]

    name = models.CharField(max_length=100)
    coffee_qty_g = models.PositiveIntegerField(
        validators=[
            MaxValueValidator(100),
            MinValueValidator(1)
        ]
        )
    grind_size = models.CharField(max_length=20, choices=GRIND, default=medium)
    water_temp_c = models.PositiveIntegerField(
        validators=[
            MaxValueValidator(100),
            MinValueValidator(1)
        ]
    )
    water_volume_ml = models.PositiveIntegerField(
        validators=[
            MaxValueValidator(999),
            MinValueValidator(1)
        ]
    )
    brew_time_mins = models.DecimalField(max_digits=4, decimal_places=2)
    products = models.ManyToManyField(Product)
    method = models.TextField()
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name
