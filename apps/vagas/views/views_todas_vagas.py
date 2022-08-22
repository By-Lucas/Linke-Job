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
from candidaturas.models.models_candidato import Candidatura

# Alertas de messagens
from django.contrib import messages
from django.contrib.messages import constants


class VagasList(ListView):
    model = Vagas
    template_name = 'todas-as-vagas.html'
    
    def get_context_data(self, *args, **kwargs):
        context = super(VagasList, self).get_context_data(*args, **kwargs)
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
        }
        return context


class VagaDetailView(DetailView):
    model = Vagas
    template_name = "detalhes-vaga.html"
    
    def get_context_data(self, *args, **kwargs):
        context = super(VagaDetailView, self).get_context_data(*args, **kwargs)
        idds = self.kwargs.get('pk')
        nomes =[]
        qtd_candidatura = 0
        candidatura_ativa = False
        for id_v in Vagas.objects.all():
            for quantidade in id_v.candidatura_set.filter(vaga=idds):
                qtd_candidatura+=1
                if quantidade.candidato == self.request.user and id_v == quantidade.vaga:
                    candidatura_ativa = True
        context['candidatura_ativa'] = candidatura_ativa
        context['quantidade'] = qtd_candidatura
        return context


def pegar_dados(request, id):
    vagas = Vagas.objects.all()
    
    cart_obj, new_obj = Candidatura.objects.new_or_get(request)
    
    qtd_candidatos = QtdCandidatura.objects.all()
    id_vaga =  request.POST.get('vaga_id')
    candidato = request.user
    nome  = request.POST.get('nome')
    requisitos_adicionais  = request.POST.get('requisitos_adicionais')
    requisitos= request.user.profileuser.sobre
    escolaridade  = request.POST.get('escolaridade')
    nomes = []
    n=0
    for id_v in Vagas.objects.all():
        for quantidade in id_v.candidatura_set.filter(vaga=id_vaga):
            nomes.append(quantidade.vaga.nome)
            n+=1
            quantidade=nomes.count(quantidade.vaga.nome)
            
    if request.method == 'POST':
        if not candidato in Candidatura.objects.all():
            candidatura = Candidatura.objects.create(
                        candidato=candidato,
                        vaga_id=id_vaga,
                        requisitos=requisitos,
            )
        
        if QtdCandidatura.objects.exists():
            cart_obj = QtdCandidatura.objects.update(vaga_candidatada_id=id_vaga, quantidade_candidatos=n)
        elif QtdCandidatura.objects.exists() and nomes[0] == int(id_vaga):
            cart_obj = QtdCandidatura.objects.update(vaga_candidatada_id=id_vaga, quantidade_candidatos=n)
        else:
            cart_obj = QtdCandidatura.objects.create(vaga_candidatada_id=id_vaga, quantidade_candidatos=n)
            
    return redirect('CandidaturaDetailView')