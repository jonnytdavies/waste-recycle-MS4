from django.shortcuts import render, redirect, HttpResponseRedirect, get_object_or_404
from django.core.urlresolvers import reverse
from .forms import CreateListing
from .models import Listing
from django.template.context_processors import csrf
from django.contrib.auth.decorators import login_required

# Create your views here.


def all_listings(request):
    listings = Listing.objects.all()
    return render(request, "listings.html", {"listings": listings})


def get_listing(request, pk):
    listing = get_object_or_404(Listing, pk=pk)
    return render(request, "listingpage.html", {'listing': listing})


@login_required
def create_or_edit_listing(request, pk=None):
    listing = get_object_or_404(Listing, pk=pk) if pk else None
    if request.method == 'POST':
        listing_form = CreateListing(request.POST,
                                     request.FILES, instance=listing)
        if listing_form.is_valid():
            listing_form.save()

            return redirect(get_listing, listing.pk)

        else:
            listing_form = CreateListing(instance=listing)

    else:
        listing_form = CreateListing()

    return render(request, 'createlisting.html',
                  {'listing_form': listing_form})
