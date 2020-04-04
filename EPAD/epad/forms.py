from django import forms
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class rateEmployeeForm(forms.ModelForm):
    class Meta:
        model = kpis
        exclude=['user']

class assignTaskForm(forms.ModelForm):
    class Meta:
        model = tasks
        exclude=['added_on','due_date','completed']

class ratesForm(forms.ModelForm):
    class Meta:
        models =kpis
        fields=['rates_for']

class progressForm(forms.ModelForm):
    class Meta:
        models = tasks
        fields=['completed']