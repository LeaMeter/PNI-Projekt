from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Korisnici

class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = Korisnici
        fields = ('email', 'password', 'role','status')

class CreateUserForm(UserCreationForm):
	class Meta:
		model = Korisnici
		fields = ['username', 'email', 'password1', 'password2', 'status']

