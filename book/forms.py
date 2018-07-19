from django import forms
from django.forms import ModelForm

from .models import Book

# Create your forms here
class BookCreationForm(ModelForm):
    class Meta:
        model = Book
        fields = [
            'title',
            'author',
            'ISBN',
            'subject',
            'sale_price',
            'vendor_price',
            'summary',
            'image',
        ]

class BookChangeForm(ModelForm):
    class Meta:
        model = Book
        fields = [
            'title',
            'author',
            'ISBN',
            'subject',
            'sale_price',
            'vendor_price',
            'summary',
            'image',
        ]
