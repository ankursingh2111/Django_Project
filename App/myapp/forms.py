#-*- coding: utf-8 -*-
from django import forms
from . import models

class LoginForm(forms.Form):
   user = forms.CharField(max_length = 100)
   password = forms.CharField(widget = forms.PasswordInput())

   def clean_username(self):
      username = self.cleaned_data.get("username")
      dbuser = Dreamreal.objects.filter(name = username)
      
      if not dbuser:
         raise forms.ValidationError("User does not exist in our db!")
      return username

class ProfileForm(forms.Form):
   name = forms.CharField(max_length = 100)
#   picture = forms.ImageFields()
