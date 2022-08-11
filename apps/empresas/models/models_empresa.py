from django.db import models
from django.urls import reverse

class Empresa(models.Model):
    #user = models.ForeignKey()
    nome = models.CharField(max_length=100, help_text='Nome da empresa')
    cnpj = models.CharField(max_length=18, null=True, blank=True, help_text='CNPJ da empresa')
    qtd_funcionario = models.IntegerField(default=0, null=True, blank=True, help_text='Quantidade de funcionarios')
    
    def __str__(self):
        return self.nome

    def get_absolute_url(self):
        return reverse('index')