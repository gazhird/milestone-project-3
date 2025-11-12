from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
from cloudinary.models import CloudinaryField
import datetime


FUEL_SELECT = [
    ('Petrol', 'Petrol'), ('Diesel', 'Diesel'), ('Electric', 'Electric'), 
    ('Hybrid', 'Hybrid'),]

YEAR_SELECT = [
    (year, year) for year in range(1980, datetime.date.today().year + 1)]


class Listing(models.Model):
    make = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    colour = models.CharField(max_length=50)
    year = models.IntegerField(choices=YEAR_SELECT)
    size = models.CharField(max_length=50)
    fuel = models.CharField(choices=FUEL_SELECT)
    slug = models.SlugField(max_length=250, unique=True, editable=False)
    seller = models.ForeignKey(
    User, on_delete=models.CASCADE, related_name="listings")
    image1 = CloudinaryField('image', default='placeholder')
    description = models.TextField()
    listed_on = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=50, default='Available', editable=False)

    def __str__(self):
        return f"{self.make} {self.model}"
    
    def save(self, *args, **kwargs):
        # save to create a id 
        if self.pk is None:
            super().save(*args, **kwargs)
        # build slug with unique url make+model+id only once
        if not self.slug:
            self.slug = slugify(f"{self.make}-{self.model}-{self.id}")
            kwargs['force_insert'] = False
            kwargs['force_update'] = True
            super().save(update_fields=['slug'])
        else:
            super().save(*args, **kwargs)

