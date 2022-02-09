from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from .models import Owner, Pet, PetOwnerMatching

class RegisterOwnerForm(ModelForm):
    class Meta:
        model = Owner
        fields = ['firstname','lastname','phone','address']

class PetForm(ModelForm):
    class Meta:
        model = Pet
        fields = ['name','age','description','type','genus']

class PetOwnerMatchForm(ModelForm):
    class Meta:
        model = PetOwnerMatching
        fields = ['ownerid','petid']