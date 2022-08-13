from django.db import models
from django.db.models.signals import pre_save, post_save, m2m_changed
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
    faixa_salarial = models.CharField(max_length=50, null=True, blank=True)
    requisitos = models.TextField(max_length=2000, null=True, blank=True)
    requisitos_adicionais = models.ManyToManyField(RequisitosVaga)
    escolaridade = models.ManyToManyField(EscolaridadeVaga)
    quantidade = models.IntegerField(default=0)
    status = models.BooleanField(default=True, help_text='Status da vaga')
    data_criacao = models.DateTimeField(auto_now = True)
    atualizado_em = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return self.nome
    
    def get_vaga_tipo(self):
        if self.tipo == 'HO':
            tipo = 'Home Office'
        if self.tipo == 'HI':
            tipo = 'Hibrido'
        if self.tipo == 'PR':
            tipo = 'Presencial'
        return tipo
    
    def get_senioridade(self):
        if self.senioridade == 'J':
            senioridade = 'Júnior'
        if self.senioridade == 'P':
            senioridade = 'Pleno'
        if self.senioridade == 'S':
            senioridade = 'Sênior'
        if self.senioridade == 'E':
            senioridade = 'Especialista'
        return senioridade
    
    class Meta():
        db_table = 'vagas'
        verbose_name = 'vaga'
        verbose_name_plural = 'vagas'
        

def m2m_changed_cart_receiver(sender, instance, action, *args, **kwargs):
    #print(action)
    #if action == 'post_add' or action == 'post_remove' or action == 'post_clear':
    #print(instance.total)
    produtos = instance.vagas.all()
    print('vagas', produtos)
    # total = 0
    # desconto = 0
    # taxas = 0
    # for produto in produtos:
    #     total += produto.preco
    #     desconto += produto.desconto / 100
    #     taxas += produto.taxa_envio_outros
    # if instance.subtotal != total:
    #     instance.subtotal = total
    #     instance.save()
        
    # instance.valor_produto = total
    # instance.desconto = desconto * total
    # instance.subtotal = total - instance.desconto
    # instance.taxa_envio_outros = taxas
    # instance.save()

m2m_changed.connect(m2m_changed_cart_receiver, sender = Vagas)