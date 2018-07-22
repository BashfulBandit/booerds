from django import forms
from django.forms import ModelForm

from .models import Promotion

# Create you forms here
class PromotionCreationForm(ModelForm):
	class Meta:
		model = Promotion
		fields = [
			'name',
			'valid_from',
			'valid_to',
			'promocode',
			'discount',
			'details',
			'frontpage',
		]

class EmailForm(forms.Form):
	subject = forms.CharField()
	message = forms.CharField(
		widget=forms.Textarea
	)
