from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.views.generic import CreateView, UpdateView, ListView, DeleteView
from django.urls import reverse_lazy

# Alertas de messagens
from django.contrib import messages
from django.contrib.messages import constants

from departamento.models.models_departamento import Departamento

class DepartamentoList(ListView):
    model = Departamento

    def get_queryset(self):
        # Só visualiza empresa logada
        empresa_logada = self.request.user.funcionario.empresa
        return Departamento.objects.filter(empresa=empresa_logada)

class DepartamentoUpdate(UpdateView):
    model = Departamento
    fields = ['departamento', 'empresa']

class DepartamentoCreate(CreateView):
    model = Departamento
    fields = ['departamento', 'empresa']

    def form_valid(self, form):
        departamento = form.save(commit=False)
        departamento.empresa = self.request.user.funcionario.empresa
        departamento.save()
        return super(DepartamentoCreate, self).form_valid(form)

class DepartamentoDelete(DeleteView):
    model = Departamento
    success_url = reverse_lazy('list_departamento')