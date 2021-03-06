from django.db import models
from datetime import datetime
from django.urls import reverse

from realtors.models import Realtor

# Create your models here.
class Listing(models.Model):

    realtor = models.ForeignKey(Realtor, on_delete=models.PROTECT)
    title = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    state = models.CharField(max_length=200)
    zipcode = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    price = models.IntegerField()
    bedrooms = models.IntegerField()
    bathrooms = models.DecimalField(max_digits=2, decimal_places=1)
    garage = models.IntegerField(default=0)
    sqft = models.IntegerField()
    lot_size = models.DecimalField(max_digits=6, decimal_places=2)
    photo_main = models.ImageField(upload_to = 'photos/%Y/%m/%d/')
    photo1 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo2 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo3 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo4 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo5 = models.ImageField(upload_to = 'photos/%Y/%m/%d/', blank=True)
    photo6 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)

    is_published = models.BooleanField(default=True)
    list_date = models.DateTimeField(default=datetime.now(), blank=True)

    class Meta:
        ordering = ['title', 'state', 'city', 'zipcode']

    def __str__(self):
        return self.title.title()

    def get_absolute_url(self):
        return reverse("Listing_detail", kwargs={"pk": self.pk})
