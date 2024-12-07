from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Usuario

class UserContCreationForm(UserCreationForm):
    SEXO_CHOICES = [ ('F','Feminino'), ('M','Masculino'), ('O','Outros'), ('N','Prefiro não dizer')]

    email = forms.EmailField(max_length=100, required=True)
    idade = forms.IntegerField(min_value=0, max_value=115)
    sexo = forms.ChoiceField(choices=SEXO_CHOICES, required=False)

    class Meta:
        model = Usuario
        fields = ('username', 'password1', 'password2', 'email', 'idade', 'sexo')

class CadastroForm(forms.ModelForm):
    SEXO_CHOICES = [
        ('M', 'Masculino'),
        ('F', 'Feminino'),
        ('O', 'Outro')
    ]

    sexo = forms.ChoiceField(choices=SEXO_CHOICES, required=True)

    class Meta:
        model = Usuario
        fields = ['username', 'email', 'idade', 'sexo']
