from django.forms import ModelForm
from django.contrib.auth.models import User
from local.us.models import (
    USStateField,
    USZipCodeField,
)

from .models import (
    Address,
    Customer,
    Vendor,
)

# Create your forms here.
class AddressCreationForm(ModelForm):
    class Meta:
        model = Address
        fields = [
            'street_address',
            'zipcode',
            'city',
            'state',
        ]

class CustomerCreationForm(ModelForm):
    class Meta:
        model = Customer
        fields = [
            'date_of_birth',
        ]
# class VendorCreationForm(ModelForm):

# Apparently we don't need a form specially 
# for updating an item.
# See the first example:
# https://docs.djangoproject.com/en/2.0/topics/forms/modelforms/