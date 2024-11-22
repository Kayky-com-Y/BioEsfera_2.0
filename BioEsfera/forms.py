from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Usuario

class UserContCreationForm(UserCreationForm):
    email = forms.EmailField(max_length=100, required=True)
    idade = forms.IntegerField(min_value=0, max_value=115)
    sexo = forms.ChoiceField(required=False)

    class Meta:
        model = Usuario
        fields = ('username', 'password1', 'password2', 'email', 'idade', 'sexo')