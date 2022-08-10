from django import forms
from django.contrib.auth.models import User
from models.models_user import ProfileUser
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError


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
    first_name = forms.CharField(max_length=30, required=True,  widget=forms.TextInput(
            attrs={
                'class':'form-control','placeholder': 'Digite seu nome aqui'
            }
        ))
    last_name = forms.CharField(max_length=30, required=True, widget=forms.TextInput(
            attrs={
                'class':'form-control','placeholder': 'Digite seu sobrenome aqui'
            }
        ))
    username = forms.CharField(max_length=120, required=True, widget=forms.TextInput(
            attrs={
                'class':'form-control','placeholder': 'Digite seu usuário aqui'
            }
        ))
    email = forms.EmailField(max_length=120, required=True, widget=forms.TextInput(
            attrs={
                'class':'form-control','placeholder': 'Digite seu email aqui'
            }
        ))
    password1 = forms.CharField(max_length=120, required=True, widget=forms.TextInput(
            attrs={
                'class':'form-control','placeholder': 'Digite sua senha aqui'
            }
        ))
    password2 = forms.CharField(max_length=120, required=True, widget=forms.TextInput(
            attrs={
                'class':'finput-group input-group-outline mb-3','placeholder': 'Confirme sua senha'
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
            'status_user',
            'sobre',
            'linkedin_user',
            'github_user',
            'instagram_user',
            'imagem_perfil',
        ]
