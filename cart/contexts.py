from django.shortcuts import get_object_or_404
from listings.models import Listing


def cart_contents(request):
    """
    Ensures that the cart contents are
    Available when rendering every page
    """

    cart = request.session.get('cart', {})

    cart_items = []
    total = 0
    listing_count = 0
    for id, quantity in cart.items():
        listing = get_object_or_404(Listing, pk=id)
        total += quantity * listing.price
        listing_count += quantity
        cart_items.append({'id': id, 'quantity': quantity,
                            'listing': listing})

    return {'cart_items': cart_items, 'total': total,
            'listing_count': listing_count}
