from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Genre, View

class NewUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

class AddGenreForm(forms.ModelForm):
    class Meta:
        model = Genre
        fields = ('genreName', )

class AddViewForm(forms.ModelForm):
    class Meta:
        model = View
        fields = ('__all__')


