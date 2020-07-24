from django import forms
from django.forms import ModelForm
from flea_market.models import *


# class UserForm(ModelForm):
#     class Meta:
#         model = User
#         fields = ['name']


class AdForm(ModelForm):
    class Meta:
        model = Ad
        fields = ['title', 'price', 'description']


class UploadImageForm(ModelForm):
    class Meta:
        model = AdImage
        fields = ['photo']
