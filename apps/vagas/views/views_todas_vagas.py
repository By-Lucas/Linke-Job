from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.views.generic import CreateView, UpdateView, ListView, DeleteView
from django.urls import reverse_lazy

from vagas.models.models_vagas import Vagas
from candidaturas.models.models_candidato import Candidatura

# Alertas de messagens
from django.contrib import messages
from django.contrib.messages import constants

class VagasList(ListView):
    model = Vagas
    template_name = 'todas-as-vagas.html'

    def get_queryset(self):
        #empresa_logada = self.request.user.funcionario.empresa
        vagas = Vagas.objects.all()
        nome_vaga= self.request.GET.get('vaga')
        print(nome_vaga)
        lista_n = []
        for nomes in vagas:
            nome = nomes.id
        
            qtd_candidatura = 0
            for quantidade in Candidatura.objects.filter(vaga_id=nome):
                qtd_candidatura+=1
                print(qtd_candidatura)
        self.request.session['qtd_candidatura'] = qtd_candidatura
        #print(dir(self.request.session))
        
        return Vagas.objects.all()