from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Complaint
from django.utils.text import slugify

class LoginForm(forms.Form):
    username=forms.CharField(max_length=100)
    password=forms.CharField(widget=forms.PasswordInput)

class RegistrationForm(UserCreationForm):
    fullname=forms.CharField(max_length=100,required=True,label="Full Name")
    class Meta:
        model=User
        fields=['fullname','username','email','password1','password2']

class ComplaintForm(forms.ModelForm):
    class Meta:
        model = Complaint
        fields = ['name', 'description', 'category', 'image']
        def save(self, *args, **kwargs):
            if not self.slug:
                self.slug = slugify(self.name)  # Generate slug from the complaint's name
            super().save(*args, **kwargs)