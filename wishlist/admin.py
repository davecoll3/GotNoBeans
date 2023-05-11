from django.contrib import admin
from .models import Wishlist


class WishlistAdmin(admin.ModelAdmin):
    # Admin for Wishlist
    model = Wishlist
    readonly_fields = ('date',)
    fields = ('user', 'product', 'date',)
    list_display = ('user', 'product', 'date',)
    ordering = ('-date',)


admin.site.register(Wishlist, WishlistAdmin)
