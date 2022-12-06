from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from mainsite.models import Course, CourseElement


class AdditionalUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password2', 'password1']


class ElementCreationForm(forms.ModelForm):
    class Meta:
        model = CourseElement
        fields = ['name', 'text']