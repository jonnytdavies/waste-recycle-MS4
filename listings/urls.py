from django.conf.urls import url
from .views import home_listings, all_listings, create_listing, get_listing, terms


urlpatterns = [
    url(r'^$', home_listings, name='home_listings'),
    url(r'^listings/$', all_listings, name='all_listings'),
    url(r'^(?P<pk>\d+)/$', get_listing, name='get_listing'),
    url(r'^createlisting/$', create_listing, name='create_listing'),
    url(r'^(?P<pk>\d+)/edit/$', create_listing, name='edit_listing'),
    url(r'^terms/$', terms, name='terms')
]
