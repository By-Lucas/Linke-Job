from django.db import models
from django.utils import timezone
from random import choice

from empresas.models.models_empresa import Empresa
from funcionarios.models.models_funcionario import Funcionario

class RequisitosVaga(models.Model):
    nome = models.CharField(max_length=100, null=True, blank=True)
    
    def __str__(self):
        return self.nome


class EscolaridadeVaga(models.Model):
    nome = models.CharField(max_length=100, null=True, blank=True)
    
    def __str__(self):
        return self.nome

def gerar_codigo():
    tamanho = 14
    valores = '1234567890'
    codigo = ''
    for i in range(tamanho):
        codigo += choice(valores)
    return codigo

class Vagas(models.Model):
    SENIORIDADE = (
        ('J', 'Junior'),
        ('P', 'Pleno'),
        ('S', 'Senior'),
        ('E', 'Especialista'),
        
    )
    
    TIPO = (
        ('HO', 'Home Office'),
        ('HI', 'Hibrido'),
        ('PR', 'Presencial'),
    )
    
    criado_por = models.CharField(max_length=50)
    empresa = models.ForeignKey(Empresa, on_delete=models.PROTECT)
    senioridade = models.CharField(max_length=20, choices=SENIORIDADE, blank=True, null=True)
    tipo = models.CharField(max_length=20, choices=TIPO, blank=True, null=True)
    codigo = models.CharField(max_length=14, default=gerar_codigo, editable=False, unique=True, blank=True, null=True)
    nome = models.CharField(max_length=60)
    faixa_salarial = models.DecimalField(decimal_places=2, max_digits=9)
    requisitos = models.TextField(max_length=2000, null=True, blank=True)
    requisitos_adicionais = models.ManyToManyField(RequisitosVaga)
    escolaridade = models.ManyToManyField(EscolaridadeVaga)
    data_criacao = models.DateTimeField(auto_now = True)
    atualizado_em = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return self.nome
    
    class Meta():
        db_table = 'vagas'
        verbose_name = 'vaga'
        verbose_name_plural = 'vagas'