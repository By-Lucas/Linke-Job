from django.shortcuts import redirect, render, HttpResponseRedirect, get_object_or_404
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import Group, User
from django.contrib.auth import views as auth_views
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView

from django.contrib import messages
from django.contrib.messages import constants

from forms.forms_user import UserForm, ProfileUserForm


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