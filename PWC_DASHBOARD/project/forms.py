from turtle import color
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
                  'from_duration', 'to_duration', 'status', 'type')

        widgets = {
            'from_duration': DatePickerInput(),
            'to_duration': DatePickerInput(),
        }


class Projectforms(ModelForm):
    class Meta:
        model = Project
        fields = ('type',)

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


class TechnologyForm(forms.Form):
    technology = forms.CharField(max_length=255, required=True)


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


class AssignAssociatesforms(ModelForm):
    class Meta:
        model = Project_Associate
        fields = ('associate',)


class CreateAssociatesForm(ModelForm):

    class Meta:
        model = Associate
        fields = ['name', 'email', 'designation', 'joindate', 'technology']
        widgets = {
            'joindate': DatePickerInput(),
        }
