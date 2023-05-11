from django.shortcuts import render, reverse, redirect, get_object_or_404

from products.models import Product
from profiles.models import UserProfile
from .models import Wishlist


def wishlist(request):
    # Renders the wishlist page
    user = UserProfile.objects.get(user=request.user)
    item = Wishlist.objects.filter(user=user)
    context = {'item': item}
    return render(request, 'wishlist/wishlist.html', context)
