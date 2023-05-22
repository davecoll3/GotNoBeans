from django.contrib import admin
from .models import Recipe


# Admin settings for Recipe model
class RecipesAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'coffee_qty',
        'grind_size',
        'brew_time',
    )

    ordering = ('name',)


admin.site.register(Recipe, RecipesAdmin)
