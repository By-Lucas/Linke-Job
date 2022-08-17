from urllib import request
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

# def candidatar(self, request):
#     template_name = 'detalhes-vaga.html'

#     user = request.user
#     candidatura_form = CandidaturaForm(request.POST)
#     if candidatura_form.is_valid():
#         candidatura_form.save()
#         messages.add_message(request, constants.SUCCESS, 'candidatura efetuada com sucesso!')
#         return redirect(reverse_lazy('profile'))
#     context = {
#         'form':candidatura_form,
#     }
#     return render(request, template_name, context)