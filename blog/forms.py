from django import forms
from .models import Message, UnapprovedNews


class ContactForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your Name'}),
            'email': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your Email'}),
            'subject': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Subject'}),
            'message': forms.Textarea(attrs={'class': 'form-control', 'rows': '5', 'placeholder': 'Message'}),
        }


class PublishForm(forms.ModelForm):
    class Meta:
        model = UnapprovedNews
        fields = '__all__'
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control ', 'placeholder': 'Title'}),
            'email': forms.TextInput(attrs={'class': 'form-control ', 'placeholder': 'Email (optional)'}),
            'reporter': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Name'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Content', 'rows': '8'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Phone'}),
            'video': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Video url (optional)'}),
            'category': forms.Select(attrs={'class': 'form-control custom-select'}),


        }
