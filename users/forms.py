from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser, Problem

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'aadhar_number', 'phone_number', 'town_name', 'district', 'mandal', 'user_type', 'password1', 'password2']

class ProblemForm(forms.ModelForm):
    class Meta:
        model = Problem
        fields = ['mandal','district','sector', 'description', 'image']