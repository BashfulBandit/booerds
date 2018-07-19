from django.db import models
from django.urls import reverse

from users.models import Vendor

# Create your models here.

class Book(models.Model):
    title = models.CharField(
        max_length=255,
        blank=False
    )
    author = models.CharField(
        max_length=255,
        blank=False
    )
    ISBN = models.CharField(
        max_length=13,
        blank=False
    )
    subject = models.CharField(
        max_length=255
    )
    sale_price = models.DecimalField(
        decimal_places=2,
        max_digits=10,
        blank=False
    )
    vendor_price = models.DecimalField(
        decimal_places=2,
        max_digits=10,
        blank=False
    )
    summary = models.TextField(
        blank=True
    )
    image = models.ImageField(
        upload_to="book/img/",
        blank=True
    )
    featured = models.BooleanField(
        default=False
    )
    vendor = models.ForeignKey(
        Vendor,
        on_delete=models.CASCADE,
        null=True,
        related_name='book',
    )

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('book:details', kwargs={'id': self.id})

    def add_to_cart_url(self):
        return reverse('cart:add_to_cart', kwargs={'id': self.id})

    def delete_from_cart_url(self):
        return reverse('cart:delete_from_cart', kwargs={'id': self.id})
