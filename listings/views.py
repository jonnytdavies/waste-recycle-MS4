from django.shortcuts import render, redirect, get_object_or_404
from django.core.urlresolvers import reverse
from listings.forms import CreateListing
from .models import Listing
from django.template.context_processors import csrf
from django.contrib.auth.decorators import login_required

# Create your views here.


def home_listings(request):
    listings = Listing.objects.all()
    return render(request, "homepage.html", {"listings": listings})


def all_listings(request):
    listings = Listing.objects.all()
    return render(request, "listings.html", {"listings": listings})


def get_listing(request, pk):
    listing = get_object_or_404(Listing, pk=pk)
    return render(request, "listingpage.html", {'listing': listing})


@login_required
def create_listing(request):
    if request.method == 'POST':
        form = CreateListing(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect(reverse('all_listings'))
    else:
        form = CreateListing()

    return render(request, 'createlisting.html', {'form': form})


def terms(request):
    return render(request, "terms.html")
