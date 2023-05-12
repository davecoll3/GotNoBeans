from django.contrib import admin
from .models import Wishlist, WishlistItem


class WishlistAdmin(admin.ModelAdmin):
    # Admin for Wishlist
    model = WishlistItem
    readonly_fields = ('date',)
    fields = ('wishlist', 'product', 'date',)
    list_display = ('wishlist', 'product', 'date',)
    ordering = ('wishlist',)


admin.site.register(Wishlist)
admin.site.register(WishlistItem, WishlistAdmin)
