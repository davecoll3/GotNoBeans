from django.shortcuts import render, reverse, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from products.models import Product
from profiles.models import UserProfile
from .models import Wishlist


def wishlist(request):
    # Renders the wishlist contents page
    return render(request, 'wishlist/wishlist.html')


def add_to_wishlist(request, product_id):
    # Add product to the wishlist
    user = UserProfile.objects.get(user=request.user)
    product = get_object_or_404(Product, pk=product_id)
    existing_wishlist = wishlist.objects.filter(user=user, product=product).exists()

    if not existing_wishlist:
        wishlist_product = Wishlist.objects.create(
            user=user,
            product=product
        )
        messages.success(request, f'You have added {wishlist_product} to your wishlist.')
        return redirect(reverse('product_detail', args=[item.id]))
    else:
        wishlist_product = Wishlist.objects.get(
            user=user,
            product=product
        )
        wishlist_product.delete()
        messages.info(request, 'Removed from wishlist')
        return redirect(reverse('product_detail', args=[item.id]))


def remove_from_wishlist(request, book_id):
    # Remove product from the wishlist
    user = UserProfile.objects.get(user=request.user)
    product = get_object_or_404(Product, pk=product_id)
    wishlist_item = Wishlist.objects.get(user=user, product=product)
    wishlist_item.delete()
    messages.success(request, f'You have removed {product.name} from your wishlist.')
