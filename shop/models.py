from django.db import models
from django.contrib.auth.models import User
from localflavor.us.models import (
	USStateField,
	USZipCodeField,
)

# Create your models here.
class Address(models.Model):
	street_address = models.CharField(max_length=100, blank=False)
	zipcode = USZipCodeField(blank=False)
	city = models.CharField(max_length=50, blank=False)
	state = USStateField(blank=False)

	def __str__(self):
		return self.street_address

class Customer(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE, blank=False)
	address = models.OneToOneField(Address, on_delete=models.CASCADE, blank=False)
	is_customer = models.BooleanField(default=True)
	is_vendor = models.BooleanField(default=False)
	# Below will be the other attributes like:
	# 	cart = models.OneToOneField(Cart, on_delete=models.CASCADE)
	# 	orders = models.OneToManyField(Order, on_delete=models.CASCADE)

	def __str__(self):
		return self.user.email

class Vendor(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE, blank=False)
	address = models.OneToOneField(Address, on_delete=models.CASCADE, blank=False)
	is_customer = models.BooleanField(default=False)
	is_vendor = models.BooleanField(default=True)
	# Below will be the other attributes like:
	# 	books = models.OneToManyField(Book, on_delete=models.CASCADE)

	def __str__(self):
		return self.user.email
# Other classes to define.
# Book
# Cart
# Order
# Promotion
