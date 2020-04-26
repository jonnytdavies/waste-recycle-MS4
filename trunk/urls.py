from django.conf.urls import url
from .views import view_trunk, add_to_trunk, delete_item


urlpatterns = [
    url(r'^$', view_trunk, name='view_trunk'),
    url(r'^add/(?P<id>\d+)', add_to_trunk, name='add_to_trunk'),
    url(r'^delete/(?P<id>\d+)', delete_item, name='delete_item')
]
