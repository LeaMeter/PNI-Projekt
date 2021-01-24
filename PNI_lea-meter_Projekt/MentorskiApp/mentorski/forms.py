from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from .models import Korisnici, Upisi, Predmeti

class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = Korisnici
        fields = ('email', 'password', 'role','status')

class CreateUserForm(UserCreationForm):
	class Meta:
		model = Korisnici
		fields = ['username', 'email', 'password1', 'password2', 'status']

class UpisForm(ModelForm):
    class Meta:
        model = Upisi
        fields = ['predmet','student']
        widgets = {'predmet': forms.HiddenInput(),'student': forms.HiddenInput()}

class PredmetForm(ModelForm):
    class Meta:
        model = Predmeti
        fields = '__all__'