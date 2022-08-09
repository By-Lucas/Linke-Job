from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView

# Alertas de messagens
from django.contrib import messages
from django.contrib.messages import constants

from .models.models_empresa import Empresa

class EmpresaCreate(CreateView):
    model = Empresa
    fields = ['nome', ]

    def form_valid(self, form):
        obj = form.save()
        #funcionario = self.request.user.funcionario # Funcionario logado
        #funcionario.empresa = obj
        obj.save()
        return HttpResponse('OK')

class EmpresaEdit(UpdateView):
    model = Empresa
    fields = ['nome', ]
