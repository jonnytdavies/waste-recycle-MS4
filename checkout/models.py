from django.db import models
from listings.models import Listing


# Model for the checkout form
class Order(models.Model):
    full_name = models.CharField(max_length=60, blank=False)
    street_address1 = models.CharField(max_length=60, blank=False)
    street_address2 = models.CharField(max_length=60, blank=True)
    city = models.CharField(max_length=40, blank=False)
    postcode = models.CharField(max_length=15, blank=True)
    county = models.CharField(max_length=40, blank=True)
    phone_number = models.CharField(max_length=15, blank=False)
    date = models.DateField()

    def __str__(self):
        return "{0}-{1}-{2}".format(self.id, self.date, self.full_name)


class OrderLineItem(models.Model):
    order = models.ForeignKey(Order, null=False)
    listing = models.ForeignKey(Listing, null=False)
    quantity = models.IntegerField(blank=False)

    def __str__(self):
        return "{0} {1} {2}".format(self.quantity, self.listing.title, self.listing.price)
