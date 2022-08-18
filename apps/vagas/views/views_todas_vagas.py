from multiprocessing import context
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.views.generic import CreateView, UpdateView, ListView, DeleteView, DetailView, TemplateView, View
from django.urls import reverse_lazy

from django.core.paginator import Paginator, InvalidPage
from django.db.models import Q

from vagas.models.candidaturas_vaga import QtdCandidatura
from vagas.models.models_vagas import Vagas
from candidaturas.models.models_qtd_candidaturas import QuatidadeCandidatura

# Alertas de messagens
from django.contrib import messages
from django.contrib.messages import constants


class VagasList(ListView):
    model = Vagas
    template_name = 'todas-as-vagas.html'
    
    def get_context_data(self, **kwargs):
        context = super(VagasList, self).get_context_data(**kwargs)
        vagas = Vagas.objects.all()

        # Campo de pesquisa
        queryset = self.request.GET.get('q')
        if queryset:
            vagas = Vagas.objects.filter(
                Q(nome__icontains=queryset)|
                Q(faixa_salarial__icontains=queryset)|
                Q(senioridade__icontains=queryset)|
                Q(tipo__icontains=queryset)|
                Q(empresa__nome__icontains=queryset)
            )
        if not vagas:
            messages.add_message(self.request, constants.WARNING, f'Nenhuma vaga disponivel')

        # Paginação
        ITEMS_PER_PAGE = 8
        page = self.request.GET.get('page')
        paginator = Paginator(vagas, ITEMS_PER_PAGE)
        total = paginator.count
        vagas = paginator.get_page(page)
        try:
            vagas_pages = paginator.page(page)
        except InvalidPage:
            vagas_pages = paginator.page(1)

        
        context = {
            'vagas': vagas,
            'vagas_pages': vagas_pages,
            'count_candidatura': QuatidadeCandidatura.objects.all()
        }
        
        return context


#Class Based View
class VagaDetailView(DetailView):
    model = Vagas
    template_name = "detalhes-vaga.html"


def pegar_dados(request, id):
    vagas = Vagas.objects.all()
    qtd_candidatos = QtdCandidatura.objects.all()
    #if request.method == 'POST':
    #print(dir(qtd_candidatos))
    date_insert  = request.POST.get('nome')
    vaga_id =  request.POST.get('id')
    #print(date_insert)
    lista = []
    n=0
    for vaga_ids in vagas:
        ids_ = vaga_ids
        for cand in vaga_ids.candidatura_set.filter(vaga=ids_):
                n+=1
                lista.append(cand.vaga.nome)
        print(lista)
        if QtdCandidatura.objects.exists():
                qd_candidatos = QtdCandidatura.objects.update(vaga_candidatada=vaga_id, quantidade_candidatos=n)
        else:
            qd_candidatos = QtdCandidatura.objects.create(vaga_candidatada=vaga_id, quantidade_candidatos=n)
            
    print(n)
    print(lista)
    

    return HttpResponse('OK')