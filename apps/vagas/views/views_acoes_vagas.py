from multiprocessing import context
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.views.generic import CreateView, UpdateView, ListView, DeleteView, DetailView, TemplateView, View
from django.urls import reverse_lazy

from vagas.models.models_vagas import Vagas


# Cada empresa verá apenas seus funcionários
class ListVagasOn(ListView):
    model = Vagas
    template_name='vagas_admin/empresa-vaga.html'
    
    def get_queryset(self):
        empresa_logada = self.request.user.funcionario.empresa
        return Vagas.objects.filter(empresa=empresa_logada)


class CreateVaga(CreateView):
    model = Vagas
    template_name='vagas_admin/create-vaga.html'
    fields = [
        'empresa', 'senioridade', 'tipo', 'nome', 'faixa_salarial',
        'requisitos', 'requisitos_adicionais', 'escolaridade', 'quantidade',
        'status'
    ]
    
    def form_valid(self, form):
        #Enviar o commit mas nao salvar no banco ate ser feito algumas coisas antes
        funcionario = form.save(commit=False)
        # Cria um usuario com nome e sobrenome junto
        username = self.request.user.username
        print(username)
        
        funcionario.empresa = self.request.user.funcionario.empresa
        funcionario.user = Vagas.objects.create(criado_por=username)
        funcionario.save()
        return super(VagaCreate, self).form_valid(form)


class UpdateVaga(UpdateView):
    model = Vagas
    template_name='vagas_admin/edit-vaga.html'
    fields = [
        'empresa', 'senioridade', 'tipo', 'nome', 'faixa_salarial',
        'requisitos', 'requisitos_adicionais', 'escolaridade', 'quantidade',
        'status'
    ]


class DeleteVaga(DeleteView):
    model = Vagas
    success_url = reverse_lazy('todas_vagas')