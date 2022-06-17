from django.forms.models import ModelForm
from django.contrib.auth import get_user_model
from django import forms
User = get_user_model()


class ManagerForm(ModelForm):
    
    class Meta:
        model = User
        fields = ('email',)
        labels = {
            'email': '',
        }
    
        widgets = {
            'email': forms.EmailInput(attrs={'placeholder': 'Enter Email Address Of Manager'})
        }


class Updateuser(ModelForm):
    class Meta:
        model = User
        fields = ['name', 'username',  'designation']
