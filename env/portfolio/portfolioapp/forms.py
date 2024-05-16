from django import forms
from .models import Message
from django.forms import ModelForm, TextInput, Textarea, EmailInput


class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['name', 'email', 'message']

        widgets = {
            'name': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Full Name'
            }),
            'email': EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Email'
            }),
            'message': Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Message'
            })
        }