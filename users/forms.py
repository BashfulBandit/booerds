from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import User

class UserRegistrationForm(UserCreationForm):

	class Meta(UserCreationForm.Meta):
		model = User
		fields = (
			'name',
			'email',
			'date_of_birth',
			'address',
			'zipcode',
			'city',
			'state',
			'user_type',
		)

	def save(self, commit=True):
        # Clean form input.
		user = super(UserRegistrationForm, self).save(commit=False)
        # Capture user input.
		user.email = self.cleaned_data['email']
		user.name = self.cleaned_data['name']
		user.user_type = self.cleaned_data['user_type']
		user.date_of_birth = self.cleaned_data['date_of_birth']
		user.address = self.cleaned_data['address']
		user.zipcode = self.cleaned_data['zipcode']
		user.city = self.cleaned_data['city']
		user.state = self.cleaned_data['state']
        # If safe store data in DB.
		if commit:
			user.save()
			return user

class UserUpdateForm(UserChangeForm):

	class Meta:
		model = User
		fields = (
			'name',
			'email',
			'address',
			'zipcode',
			'city',
			'state',
		)
