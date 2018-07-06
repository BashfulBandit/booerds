from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import User

class UserRegistrationForm(UserCreationForm):
	email = forms.EmailField(
		label='Email Address',
		required=True,
	)
	name = forms.CharField(
		label='Full Name',
		max_length=254,
		required=True,
	)
	date_of_birth = forms.DateField(
		label='Date of Birth',
		required=True,
	)
	address = forms.CharField(
		label='Street Address',
		required=True,
	)
	zipcode = forms.CharField(
		label='Zip Code',
		required=True,
	)
	city = forms.CharField(
		label='City',
		required=True,
	)
	state = forms.CharField(
		label='State',
		required=True,
	)

	class Meta(UserCreationForm.Meta):
		model = User
		fields = (
			'email',
			'name',
			'date_of_birth',
			'address',
			'zipcode',
			'city',
			'state',
		)

	def save(self, commit=True):
		user = super(UserRegistrationForm, self).save(commit=False)
		user.email = self.cleaned_data['email']
		user.name = self.cleaned_data['name']
		user.date_of_birth = self.cleaned_data['date_of_birth']
		user.address = self.cleaned_data['address']
		user.zipcode = self.cleaned_data['zipcode']
		user.city = self.cleaned_data['city']
		user.state = self.cleaned_data['state']
		if commit:
			user.save()
		return user

# class UserUpdateForm(UserChangeForm):
#
# 	class Meta:
# 		model = User
# 		fields = (
# 			'name',
# 			'email',
# 			'address',
# 			'zipcode',
# 			'city',
# 			'state',
# 		)
