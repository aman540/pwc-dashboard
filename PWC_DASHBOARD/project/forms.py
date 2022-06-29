from django.forms import DateInput, TextInput
from dataclasses import field
from django.forms import ModelForm
from .models import*
from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UsernameField
from .widget import DatePickerInput
User = get_user_model()


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['name', 'username', 'email', 'password1', 'password2']
        # field_classes = {'username': UsernameField}


class ProjectUpdateforms(ModelForm):
    class Meta:
        model = Project
        fields = ('title', 'client', 'description',
                  'from_duration', 'to_duration', 'status',)

        widgets = {
            'from_duration': DatePickerInput(),
            'to_duration': DatePickerInput(),
        }

# class Projectforms(ModelForm):
#     class Meta:
#         model = Project
#         fields = ('status',)

#         widgets = {
#             'from_duration': DatePickerInput(),
#             'to_duration': DatePickerInput(),
#         }


class ProjectStatusUpdateForm(ModelForm):
    class Meta:
        model = Project
        fields = ("status",)


# class ProjectPhaseUpdateForm(ModelForm):
#     class Meta:
#         model = Project
#         fields = ("phase",)


class Technologyforms(ModelForm):
    class Meta:
        model = Technoproject
        fields = ("technology",)


class PhaseDurationForm(ModelForm):
    class Meta:
        model = PhaseDurationOfProject
        fields = ('phase', 'from_date', 'to_date')
        widgets = {
            'from_date': DatePickerInput(),
            'to_date': DatePickerInput(),
        }


class Associatesforms(ModelForm):
    class Meta:
        model = Associates
        fields = ("name", "email", "designation",)
