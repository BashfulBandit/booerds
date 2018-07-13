from django.db import models
from django.contrib.auth.models import AbstractUser
# from django.contrib.auth.models import User
from localflavor.us.models import (
    USStateField,
    USZipCodeField,
)
from django.urls import reverse

# Create your models here.
class User(AbstractUser):
    is_customer = models.BooleanField('customer status', default=False)
    is_vendor = models.BooleanField('vendor statuc', default=False)
    street_address = models.CharField(max_length=100, blank=False)
    zipcode = USZipCodeField(blank=False)
    city = models.CharField(max_length=50, blank=False)
    state = USStateField(blank=False)
    date_of_birth = models.DateField(blank=False)

class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)

class Vendor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
