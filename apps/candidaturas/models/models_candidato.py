from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from random import choice

from usuarios.models.models_user import ProfileUser
from vagas.models.models_vagas import Vagas
from vagas.models.candidaturas_vaga import QtdCandidatura
from .models_qtd_candidaturas import QuatidadeCandidatura


class CandidaturaManager(models.Manager):
    def new_or_get(self, request):
        cand_id = request.session.get('candidatura_id', None)
        print('KKKKKKKK', cand_id)
        id_vaga = request.POST.get('id')
        qs = self.get_queryset().filter(id=cand_id)
        
        if qs.count() == 1:
            nomes =[]
            n = 0
            for id_v in Vagas.objects.all():
                for quantidade in id_v.candidatura_set.filter(vaga=id_vaga):
                    nomes.append(quantidade.vaga.id)
                    n+=1
            
            new_obj = False
            if not QtdCandidatura.objects.exists():
                cart_obj = QtdCandidatura.objects.create(vaga_candidatada_id=id_vaga, quantidade_candidatos=n)
                print(nomes[0], 'agora foi criado')
            else:
                cart_obj = QtdCandidatura.objects.update(vaga_candidatada_id=id_vaga, quantidade_candidatos=n)
                print(nomes[0], 'agora foi atualizado')
        else:
            print('KKK agora foi criado')
            
            cart_obj = QtdCandidatura.objects.create(vaga_candidatada_id=id_vaga, quantidade_candidatos=1)
            new_obj = True
            request.session['candidatura_id'] = cart_obj
        return cart_obj, new_obj
    
    def get(self, request):
        cart_id = request.session.get("candidatura_id", None)
        requestsession['cart_items'] = cart_id
        #qs = self.get_queryset().filter(id=cart_id)
        return cart_id
    
    # def new(self, id_ = None):
    #     vaga_id = None
    #     if not id_ is None:
    #         if user.is_authenticated:
    #             vaga_id=id_
    #     return self.model.objects.create(vaga=vaga_id)

def gerar_codigo():
    tamanho = 14
    valores = '1234567890'
    codigo = ''
    for i in range(tamanho):
        codigo += choice(valores)
    return codigo

class RequisitosCandidatura(models.Model):
    nome = models.CharField(max_length=100, null=True, blank=True)
    
    def __str__(self):
        return self.nome


class EscolaridadeCandidatura(models.Model):
    nome = models.CharField(max_length=100, null=True, blank=True)
    
    def __str__(self):
        return self.nome


class Candidatura(models.Model):
    codigo = models.CharField(max_length=14, default=gerar_codigo, editable=False, unique=True, blank=True, null=True)
    candidato = models.ForeignKey(User, on_delete=models.CASCADE)
    vaga = models.ForeignKey(Vagas, on_delete=models.CASCADE)
    requisitos = models.TextField(max_length=2000, null=True, blank=True)
    requisitos_adicionais = models.ManyToManyField(RequisitosCandidatura, null=True, blank=True)
    escolaridade = models.ForeignKey(EscolaridadeCandidatura, on_delete=models.CASCADE, null=True, blank=True)
    escolhido = models.BooleanField(default=False)
    atualizado_em = models.DateTimeField(default=timezone.now)
    data_cadastro = models.DateTimeField(auto_now = True)
    
    objects = CandidaturaManager()

    def __str__(self):
        return f'{self.candidato} : {self.codigo}'
    
    class Meta():
        db_table = 'candidatura'
        verbose_name = 'candidatura'
        verbose_name_plural = 'candidaturas'