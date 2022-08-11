from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import Group
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView

from django.contrib import messages
from django.contrib.messages import constants

from ..forms.forms_user import UserForm, ProfileUserForm, SignUpForm


class SignUpView(CreateView):
    form_class = SignUpForm
    success_url = reverse_lazy('index')
    template_name = 'register/sign-up.html'

    def form_valid(self, form):
        grupo = get_object_or_404(Group, name='usuario')

        url = super().form_valid(form)
        self.object.groups.add(grupo)
        self.object.save()

        username = form.cleaned_data['username']
        password = form.cleaned_data['password1']
        print('Senha:',password)
        logando = authenticate(self.request, username=username, password=password)
        login(self.request, logando)
        messages.add_message(self.request, constants.SUCCESS, f'Usuário {username} cadastrado e logado com sucesso!')
        return url

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['titulo'] = 'Cadastre-se'
        context['botao'] = 'Cadastrar'
        return context


class ProfileUpdateView(TemplateView):
    template_name = 'profile/edit-profile.html'
    def get(self, request):
        user = request.user
        profile = user.profileuser
        user_form = UserForm(instance=user)
        profile_form = ProfileUserForm(instance=profile)
        context = {
            'user_form': user_form,
            'profile_form': profile_form,
        }
        return render(request, self.template_name, context)

    def post(self, request):
        user = request.user
        profile = user.profileuser
        user_form = UserForm(request.POST, instance=user)
        profile_form = ProfileUserForm(request.POST, request.FILES, instance=profile)
        if user_form.is_valid() and profile_form.is_valid():# and config_form.is_valid()
            user_form.save()
            profile_form.save()
            messages.add_message(request, constants.SUCCESS, 'Perfil editado com sucesso!')
            return redirect(reverse_lazy('profile'))
        context = {
            'user_form':user_form,
            'profile_form':profile_form,
        }
        return self.render_to_response(context)


class profileView(TemplateView):
    template_name = 'profile/profile.html'
    def get(self, request):
        if not self.request.user.is_authenticated:
            messages.error(request, 'Para acessar o perfil, faça o login.')
            return redirect('home')
        else:
            user = request.user
            profile = user.profileuser
            user_form = UserForm(instance=user)
            profile_form = ProfileUserForm(instance=profile)
        context = {
            'user_form': user_form,
            'profile_form': profile_form,
        }
        return render(request, self.template_name, context)