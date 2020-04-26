from django.shortcuts import get_object_or_404
from listings.models import Listing


def trunk_contents(request):
    """
    Ensures that the trunk contents are
    Available when rendering every page
    """

    trunk = request.session.get('trunk', {})

    trunk_items = []
    total = 0
    listing_count = 0
    for id, quantity in trunk.items():
        listing = get_object_or_404(Listing, pk=id)
        total += quantity * listing.price
        listing_count += quantity
        trunk_items.append({'id': id, 'quantity': quantity,
                            'listing': listing})

    return {'trunk_items': trunk_items, 'total': total,
            'listing_count': listing_count}
