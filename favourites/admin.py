from django.contrib import admin
from .models import FavouritesList, FavouritesListItem


class FavouritesAdmin(admin.ModelAdmin):
    # Admin for FavouritesListItem
    model = FavouritesListItem
    fields = ('favourites', 'product',)
    list_display = ('favourites', 'product',)
    ordering = ('favourites',)


admin.site.register(FavouritesList)
admin.site.register(FavouritesListItem, FavouritesAdmin)
