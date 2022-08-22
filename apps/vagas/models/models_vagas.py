from django.db import models
from django.db.models.signals import pre_save, post_save, m2m_changed
from django.utils import timezone
from django.urls import reverse, reverse_lazy
from random import choice

from empresas.models.models_empresa import Empresa
from candidaturas.models.models_qtd_candidaturas import QuatidadeCandidatura
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

def upload_to(instance ,filename):
    return 'vagas/{username}/{filename}'.format(
        username=instance.nome, filename=filename)


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
    image = models.ImageField(default='vaga.npg', upload_to=upload_to, null=True, blank=True)
    criado_por = models.CharField(max_length=50)
    empresa = models.ForeignKey(Empresa, on_delete=models.PROTECT)
    senioridade = models.CharField(max_length=20, choices=SENIORIDADE, blank=True, null=True)
    tipo = models.CharField(max_length=20, choices=TIPO, blank=True, null=True)
    codigo = models.CharField(max_length=14, default=gerar_codigo, editable=False, unique=True, blank=True, null=True)
    nome = models.CharField(max_length=60)
    faixa_salarial = models.DecimalField(max_digits=9, decimal_places=2, null=True, blank=True)
    requisitos = models.TextField(max_length=2000, null=True, blank=True)
    requisitos_adicionais = models.ManyToManyField(RequisitosVaga, blank=True, null=True)
    escolaridade = models.ForeignKey(EscolaridadeVaga, on_delete=models.PROTECT, null=True, blank=True)
    status = models.BooleanField(default=True, help_text='Vaga ativa / inativa', null=True, blank=True)
    data_criacao = models.DateTimeField(auto_now = True)
    atualizado_em = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return self.nome
    
    def get_vaga_tipo(self):
        if self.tipo == 'HO':
            tipo = 'Home Office'
        elif self.tipo == 'HI':
            tipo = 'Hibrido'
        elif self.tipo == 'PR':
            tipo = 'Presencial'
        else:
            tipo = 'Local não informado'
        return tipo
    
    def get_senioridade(self):
        if self.senioridade == 'J':
            senioridade = 'Júnior'
        elif self.senioridade == 'P':
            senioridade = 'Pleno'
        elif self.senioridade == 'S':
            senioridade = 'Sênior'
        elif self.senioridade == 'E':
            senioridade = 'Especialista'
        else:
            senioridade = 'Senioridade não informado'
        return senioridade
    
    def get_absolute_url(self):
        return reverse('ListVagasOn')
    
    class Meta():
        db_table = 'vagas'
        verbose_name = 'vaga'
        verbose_name_plural = 'vagas'