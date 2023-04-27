from django.contrib import admin
from .models import Product, Category


class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'sku',
        'category',
        'price',
        'rating',
        'image',
    )

    ordering = ('name',)


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )

    ordering = ('name',)


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
