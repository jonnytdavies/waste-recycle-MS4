from django.conf.urls import url, include
from .views import all_listings, create_or_edit_listing, get_listing


urlpatterns = [
    url(r'^$', all_listings, name='all_listings'),
    url(r'^(?P<pk>\d+)/$', get_listing, name='get_listing'),
    url(r'^createlisting/$', create_or_edit_listing, name='create_listing'),
    url(r'(?P<pk>\d+)/edit/$', create_or_edit_listing, name='edit_listing')
]
