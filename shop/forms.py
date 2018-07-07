from django import forms
from django.contrib.auth.forms import (
	UserCreationForm
)

from .models import MyUser

class MyUserCreationForm(UserCreationForm):
	email = forms.EmailField(
		label='Email Address',
		required=True,
	)
	full_name = forms.CharField(
		label='Full Name',
		max_length=254,
		required=True,
	)

	class Meta(UserCreationForm.Meta):
		model = MyUser
		field = [
			'email',
			'full_name',
		]

	def save(self, commit=True):
		user = super(MyUserCreationForm, self).save(commit=False)
		user.email = self.cleaned_data['email']
		user.full_name = self.cleaned_data['full_name']
		if commit:
			user.save()
		return user
