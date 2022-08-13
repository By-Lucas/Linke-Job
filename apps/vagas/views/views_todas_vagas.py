from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.views.generic import CreateView, UpdateView, ListView, DeleteView, DetailView, TemplateView, View
from django.urls import reverse_lazy

from vagas.models.models_vagas import Vagas
from candidaturas.models.models_candidato import Candidatura

# Alertas de messagens
from django.contrib import messages
from django.contrib.messages import constants


class VagasList(ListView):
    model = Vagas
    template_name = 'todas-as-vagas.html'
    
    def get_context_data(self, **kwargs):
        context = super(VagasList, self).get_context_data(**kwargs)
        # FILTER BY CURRENT MONTH, USER
        vagas = Vagas.objects.all()
        if self.request.GET.get('vaga_id'):
            print('passou')
            date_insert  = self.request.GET.get('vaga_id')
            print(date_insert)
            filter_ = filter_.filter(vaga_id=date_insert)
        for vaga_ids in vagas:
            vaga_id = vaga_ids.id
            qtd_candidatura = []
            
            for quantidade in Candidatura.objects.filter(vaga_id=vaga_id):
                qtd_candidatura.append(quantidade.vaga.nome)
            result = [vaga_ids.nome, qtd_candidatura.count(vaga_ids.nome)]
        
            
            print(result)
            context['vaga_nome'] = vaga_ids.nome
            self.request.session['vaga_count'] = qtd_candidatura.count(vaga_ids.nome)
        return context
    
    def get_queryset(self):
        #empresa_logada = self.request.user.funcionario.empresa
        vagas = Vagas.objects.all()
        
        return Vagas.objects.all()
    

#Class Based View
class VagaDetailView(DetailView):
    model = Vagas
    template_name = "detalhes-vaga.html"
