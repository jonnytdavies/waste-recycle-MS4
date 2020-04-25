from django.conf.urls import url
from .views import create_listing_view


urlpatterns = [
    url(r'^create-listing/$', create_listing_view, name='create_listing_view'),
]
