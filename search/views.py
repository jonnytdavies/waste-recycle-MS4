from django.shortcuts import render
from listings.models import Listing


def do_search(request):
    listings = Listing.objects.filter(location__icontains=request.GET['q'])
    return render(request, "listings.html", {"listings": listings})
