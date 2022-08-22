from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import CreateView, UpdateView, ListView, DeleteView, DetailView, TemplateView, View
from django.urls import reverse_lazy

from django.contrib import messages
from django.contrib.messages import constants

from vagas.forms import CreateVagasForm, RequisitoForm
from vagas.models.models_vagas import Vagas, RequisitosVaga


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
    form_class = CreateVagasForm

    def is_valid(self, form):
        form = CreateVagasForm(request.POST, request.FILES)
        form_requisito = RequisitoForm(request.POST)
        
        if form.is_valid():
            nome = self.request.POST.get('nome')
            form = form.save(commit=False)
            username = self.request.user.username
            empresa_logada = self.request.user.funcionario.empresa
            form.save()
            messages.add_message(self.request, constants.SUCCESS, f'Vaga {nome.upper()} cadastrada com sucesso!')
        return redirect(reverse_lazy('ListVagasOn'))


class UpdateVaga(UpdateView):
    model = Vagas
    template_name='vagas_admin/edit-vaga.html'
    form_class = CreateVagasForm

    def is_valid(self, request):
        vaga_form = CreateVagasForm(request.POST, request.FILES)
        nome = self.request.POST.get('nome')
        if vaga_form.is_valid():
            vaga_form.save()
            messages.add_message(request, constants.SUCCESS, f'Vaga {nome.upper()} atualizada com sucesso')
            return redirect(reverse_lazy('ListVagasOn'))
        context = {
            'vaga_form':vaga_form,
        }
        return self.render_to_response(context)


class DeleteVaga(DeleteView):
    model = Vagas
    success_url = reverse_lazy('todas_vagas')
    

class CreateRequisito(CreateView):
    model = RequisitosVaga
    fields = ('nome',)
    template_name = 'vagas_admin/requisitosvaga_form.html'
    success_url = reverse_lazy('CreateRequisito')
    def is_valid(self, form):
        form = RequisitoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(self,request, constants.SUCCESS, f'Requisito {nome.upper()} atualizada com sucesso')
            return redirect(reverse_lazy('CreateRequisito'))

        context = {
            'requisitos': RequisitosVaga.objects.all()
        }
        return self.render_to_response(context)

    def get_context_data(self, **kwargs):
        context = super(CreateRequisito, self).get_context_data(**kwargs)
        context['requisitos'] = RequisitosVaga.objects.all()
        return context
    

def delete_requisito(request, id=None):
    requisito = get_object_or_404(RequisitosVaga, id=id)
    requisito.delete()
    return redirect('CreateRequisito')