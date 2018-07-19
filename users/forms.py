from django import forms
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
	first_name = forms.CharField(
        required=True
    )
	last_name = forms.CharField(
        required=True
    )
	email = forms.CharField(
        required=True
    )

	class Meta(UserCreationForm.Meta):
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
            'city',
            'state',
            'zipcode',
            'avatar',
        ]

class VendorCreationForm(ModelForm):
    class Meta:
        model = Vendor
        fields = [
            'street_address',
            'city',
            'state',
            'zipcode',
            'avatar',
        ]

class CustomerChangeForm(ModelForm):
    class Meta:
        model = Customer
        fields = [
            'street_address',
            'city',
            'state',
            'zipcode',
            'avatar',
        ]

class VendorChangeForm(ModelForm):
    class Meta:
        model = Vendor
        fields = [
            'street_address',
            'city',
            'state',
            'zipcode',
            'avatar',
        ]
