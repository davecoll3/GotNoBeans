from decimal import Decimal
from django.shortcuts import get_object_or_404
from django.conf import settings
from products.models import Product


def basket_contents(request):

    basket_items = []
    total = 0
    product_count = 0
    delivery = 0
    basket = request.session.get('basket', {})

    for item_id, quantity in basket.items():
        product = get_object_or_404(Product, pk=item_id)
        total += quantity * product.price
        product_count += quantity
        basket_items.append({
            'item_id': item_id,
            'quantity': quantity,
            'product': product,
        })

    if total == 0:
        delivery = 0
    else:
        delivery = Decimal(3.99)

    grand_total = delivery + total

    context = {
        'basket_items': basket_items,
        'total': total,
        'product_count': product_count,
        'delivery': delivery,
        'grand_total': grand_total,
    }

    return context
