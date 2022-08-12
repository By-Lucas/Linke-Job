from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError

from ..models.models_user import ProfileUser

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            'username',
            'first_name',
            'last_name',
            'email'
        ]


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=True, label='Nome:',  widget=forms.TextInput(
            attrs={
                'class':'form-control','placeholder': 'Digite seu nome aqui'
            }
        ))
    last_name = forms.CharField(max_length=30, required=True, label='Sobrenome:', widget=forms.TextInput(
            attrs={
                'class':'form-control','placeholder': 'Digite seu sobrenome aqui'
            }
        ))
    username = forms.CharField(max_length=120, required=True, label='Usuário:',widget=forms.TextInput(
            attrs={
                'class':'form-control','placeholder': 'Digite seu usuário aqui'
            }
        ))
    email = forms.EmailField(max_length=120, required=True, label='Email:', widget=forms.TextInput(
            attrs={
                'class':'form-control','placeholder': 'Digite seu email aqui', 'type': 'email'
            }
        ))
    password1 = forms.CharField(max_length=120, required=True,label='Senha:', widget=forms.TextInput(
            attrs={
                'class':'form-control','placeholder': 'Digite sua senha aqui', 'type': 'password'
            }
        ))
    password2 = forms.CharField(max_length=120, required=True, label='Confirmar senha:', widget=forms.TextInput(
            attrs={
                'class':'form-control','placeholder': 'Confirme sua senha', 'type': 'password'
            }
        ))
    
    class Meta:
        model = User
        fields = [
            'username',
            'first_name',
            'last_name',
            'email',
            'password1',
            'password2'
        ]
        
    def clean_email(self):
        email  = self.cleaned_data['email']
        if User.objects.filter(email=email ).exists():
            raise ValidationError("O email {} já está em uso" .format(email))
        return email 
    
    def clean_username(self):
        username  = self.cleaned_data['username']
        if User.objects.filter(username=username ).exists():
            raise ValidationError("O usuário {} já está em uso" .format(username))
        return username 


class ProfileUserForm(forms.ModelForm):
    class Meta:
        model = ProfileUser
        fields = [
            'idade',
            'cidade',
            'endereco',
            'numero_casa',
            'contato',
            'cpf',
            'cnpj',
            'sobre',
            'linkedin_user',
            'github_user',
            'instagram_user',
            'imagem_perfil',
        ]
