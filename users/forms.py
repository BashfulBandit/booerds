from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction
from localflavor.us.models import (
    USStateField,
    USZipCodeField,
)

from users.models import (
    User,
    Customer,
    Vendor,
)

# Create your forms here.
class CustomerRegisterForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = [
            'first_name',
            'last_name',
            'username',
            'street_address',
            'zipcode',
            'city',
            'state',
            'date_of_birth',
        ]

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_customer = True
        user.street_address = self.cleaned_data.get('street_address')
        user.zipcode = self.cleaned_data.get('zipcode')
        user.city = self.cleaned_data.get('city')
        user.state = self.cleaned_data.get('state')
        user.save()
        customer = Customer.objects.create(user=user)
        return user

class VendorRegisterForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = [
            'first_name',
            'last_name',
            'username',
            'street_address',
            'zipcode',
            'city',
            'state',
            'date_of_birth',
        ]

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_vendor = True
        user.street_address = self.cleaned_data.get('street_address')
        user.zipcode = self.cleaned_data.get('zipcode')
        user.city = self.cleaned_data.get('city')
        user.state = self.cleaned_data.get('state')
        user.save()
        vendor = Vendor.objects.create(user=user)
        return user
