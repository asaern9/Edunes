from django import forms
from .models import Message


class ContactForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control px-3 py-3', 'placeholder': 'Your Name'}),
            'email': forms.TextInput(attrs={'class': 'form-control px-3 py-3', 'placeholder': 'Your Email'}),
            'subject': forms.TextInput(attrs={'class': 'form-control px-3 py-3', 'placeholder': 'Subject'}),
            'message': forms.TextInput(attrs={'class': 'form-control px-3 py-3', 'placeholder': 'Message'}),
        }