from django.forms import ModelForm
from django.contrib.auth.models import User
from localflavor.us.models import (
    USStateField,
    USZipCodeField,
)
from django.contrib.auth.forms import UserCreationForm

from .models import (
    Customer,
    Vendor,
)

# Create your forms here.
class MyUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = [
            'first_name',
            'last_name',
            'email',
            'username',
        ]

class CustomerCreationForm(ModelForm):
    class Meta:
        model = Customer
        fields = [
            'date_of_birth',
            'street_address',
            'zipcode',
            'city',
            'state',
        ]
class VendorCreationForm(ModelForm):
    class Meta:
        model = Vendor
        fields = [
            'street_address',
            'zipcode',
            'city',
            'state',
        ]

# Apparently we don't need a form specially
# for updating an item.
# See the first example:
# https://docs.djangoproject.com/en/2.0/topics/forms/modelforms/
