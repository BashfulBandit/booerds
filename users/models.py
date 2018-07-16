from django.db import models
from django.contrib.auth.models import User
from localflavor.us.models import (
    USStateField,
    USZipCodeField,
)
from django.urls import reverse

# Create your models here.
class Customer(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name='customer',
        blank=False,
        primary_key=True
    )
    street_address = models.CharField(max_length=100, blank=False)
    zipcode = USZipCodeField(blank=False)
    city = models.CharField(max_length=50, blank=False)
    state = USStateField(blank=False)

    is_customer = models.BooleanField(default=True)
    is_vendor = models.BooleanField(default=False)

    date_of_birth = models.DateField(blank=False)

    def __str__(self):
        return self.user.email

    def get_absolute_url(self):
        return reverse('users:profile', kwargs={'id': self.user.id})

class Vendor(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name='vendor',
        blank=True,
        primary_key=True
    )
    street_address = models.CharField(max_length=100, blank=False)
    zipcode = USZipCodeField(blank=False)
    city = models.CharField(max_length=50, blank=False)
    state = USStateField(blank=False)

    is_customer = models.BooleanField(default=False)
    is_vendor = models.BooleanField(default=True)

    def __str__(self):
        return self.user.email

    def get_absolute_url(self):
        return reverse('users:profile', kwargs={'id': self.user.id})
