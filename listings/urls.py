from django.conf.urls import url, include
from .views import all_listings, create_listing_view


urlpatterns = [
    url(r'^$', all_listings, name='all_listings'),
    url(r'^create-listing/$', create_listing_view, name='create_listing_view'),
]
