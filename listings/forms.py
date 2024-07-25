from django import forms
from .models import Listing

class ListingForm(forms.ModelForm):
    class Meta:
        model = Listing
        fields = ['title','category', 'description', 'image', 'price', 'telephone_number', 'user']
        
