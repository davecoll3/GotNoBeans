from django.conf import settings


def basket_contents(request):

    basket_items = []
    total = 0
    product_count = 0
    delivery = 3.99

    grand_total = delivery + total

    context = {
        'basket_items': basket_items,
        'total': total,
        'product_count': product_count,
        'delivery': delivery,
        'grand_total': grand_total,
    }

    return context
