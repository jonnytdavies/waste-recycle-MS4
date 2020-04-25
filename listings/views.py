from django.shortcuts import render, redirect, HttpResponseRedirect
from django.core.urlresolvers import reverse
from .forms import CreateListing
from django.template.context_processors import csrf
from django.contrib.auth.decorators import login_required

# Create your views here.


@login_required
def create_listing_view(request):
    listing_form = CreateListing(request.POST)
    if listing_form.is_valid():
        listing_form.save()

    return render(request, 'listings.html', {'listing_form': listing_form})
