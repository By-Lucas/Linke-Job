from django.shortcuts import render,  get_object_or_404
from django.views.generic import CreateView, UpdateView, ListView, DeleteView, DetailView, TemplateView, View
from django.urls import reverse_lazy

from vagas.models.models_vagas import Vagas


class Admin(TemplateView):
    template_name='admin.html'
    
    
class Delete(DeleteView):
    model = Vagas
    template_name='admin-templates/delete-admin.html'
    success_url = reverse_lazy('ListVagasOn')