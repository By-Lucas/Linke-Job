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
class CandidaturaDetailView(ListView):
    model = Candidatura
    template_name = "admin-templates/minhas-candidaturas.html"

    def get_context_data(self, *args, **kwargs):
        context = super(CandidaturaDetailView, self).get_context_data(*args, **kwargs)
        return context

    def get_queryset(self):
        usuario_logado = self.request.user
        return Candidatura.objects.filter(candidato=usuario_logado)


