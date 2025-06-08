from django import forms
from .models import Client, Deal

class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ['name', 'email', 'phone', 'address']
        widgets = {
            'address': forms.Textarea(attrs={'rows': 3}),
        }

class DealForm(forms.ModelForm):
    class Meta:
        model = Deal
        fields = ['amount', 'status', 'description']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 3}),
        }