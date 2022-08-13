from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth.models import Group
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView, ListView, DetailView

from django.contrib import messages
from django.contrib.messages import constants

from candidaturas.models.models_candidato import Candidatura
from candidaturas.forms import CandidaturaForm

#Class Based View
class CandidaturaDetailView(DetailView):
    template_name = "products/detail.html"

    def get_context_data(self, *args, **kwargs):
        context = super(CandidaturaDetailView, self).get_context_data(*args, **kwargs)
        return context

    def get_object(self, *args, **kwargs):
        pk = self.kwargs.get('pk')
        instance = ProdutoModel.objects.get_by_id(pk)
        if instance is None:
            raise Http404("Esse produto não existe!")
        return instance

class FuncionariosList(DetailView):
    model = CandidaturaForm
    def get_queryset(self):
        #empresa_logada = self.request.user.funcionario.empresa
        return Funcionario.objects.all(empresa=empresa_logada)

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