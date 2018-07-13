from django.db import models
from django.urls import reverse

# Create your models here.

class Book(models.Model):
    ISBN = models.CharField(max_length=13, blank=False)
    author = models.CharField(max_length=255, blank=False)
    title = models.CharField(max_length=255, blank=False)
    image = models.ImageField(upload_to="images/", blank=True)
    subject = models.CharField(max_length=255)
    sale_price = models.DecimalField(decimal_places=2, max_digits=10, blank=False)
    vendor_price = models.DecimalField(decimal_places=2, max_digits=10, blank=False)
    summary = models.TextField(blank=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('book:details', kwargs={'id': self.id})
