from django.db import models


# Create your models here.

class Listing(models.Model):
    title = models.CharField(max_length=100, null=False, blank=False)
    description = models.TextField(max_length=500, null=False, blank=False)
    location = models.CharField(max_length=100, null=False, blank=False)
    image = models.ImageField(upload_to='images', blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.title
