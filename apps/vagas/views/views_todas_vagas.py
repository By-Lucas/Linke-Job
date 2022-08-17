from multiprocessing import context
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.views.generic import CreateView, UpdateView, ListView, DeleteView, DetailView, TemplateView, View
from django.urls import reverse_lazy

from django.core.paginator import Paginator, InvalidPage
from django.db.models import Q

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
            messages.add_message(self.request, constants.WARNING, f'Vaga "{queryset.upper()}" não encontrada')

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
            

        if self.request.GET.get('vaga_id'):
            print('passou')
            date_insert  = self.request.GET.get('vaga_nome')
            print(date_insert)
            filter_ = filter_.filter(vaga_id=date_insert)
        lista = []
        for vaga_ids in vagas:
            for cand in vaga_ids.candidatura_set.filter(vaga_id=vaga_ids):
                if str(vaga_ids.nome) in cand.vaga.nome:
                    lista.append(cand.vaga.nome)
                    #lista.count(lista)
        print(lista)
        vaga_id = vaga_ids.id
        qtd_candidatura = []
            

        context = {
            'qtd':lista,
            'total': total,
            'vagas': vagas,
            'vagas_pages': vagas_pages
        }
        
        return context
    
    # def get_queryset(self):
    #     vagas = Vagas.objects.all()
    #     queryset = self.request.GET.get('q')
    #     if queryset:
    #         vagas = Vagas.objects.filter(
    #             Q(nome__icontains=queryset)|
    #             Q(faixa_salarial__icontains=queryset)|
    #             Q(senioridade__icontains=queryset)|
    #             Q(tipo__icontains=queryset)|
    #             Q(empresa__nome__icontains=queryset)
    #         )
    #     if not vagas:
    #         messages.warning(self.request, 'Nenhum sorteio encontrado')
    #         #empresa_logada = self.request.user.funcionario.empresa
        
    #     return vagas
    

#Class Based View
class VagaDetailView(DetailView):
    model = Vagas
    template_name = "detalhes-vaga.html"



def pegar_dados(request, id):
    vagas = Vagas.objects.all()
    qtd_candidatos = QuatidadeCandidatura.objects.all()
    #if request.method == 'POST':
    #print(dir(qtd_candidatos))
    date_insert  = request.GET.get('nome')
    vaga_id =  request.GET.get('id')
    #print(date_insert)
    lista = []
    n=0
    for vaga_ids in vagas:
        for cand in vaga_ids.candidatura_set.filter(vaga_id=vaga_ids):
            if str(date_insert) in cand.vaga.nome:
                n+=1
                lista.append(cand.vaga.nome)
    print()
    if QuatidadeCandidatura.objects.filter(vaga=date_insert):
        qd_candidatos = QuatidadeCandidatura.objects.update(id=vaga_id, vaga=lista[0], quantidade_candidatos=n)
    else:
        qd_candidatos = QuatidadeCandidatura.objects.create(id=vaga_id, vaga=lista[0], quantidade_candidatos=n)
                
    print(n)
    print(lista)


    return HttpResponse('ok')