from django.db import models
from django.urls import reverse

def upload_to(instance ,filename):
    return 'empresas/{name}/{filename}'.format(
        name=instance.nome, filename=filename)
    
class Empresa(models.Model):
    foto = models.ImageField(default='vaga.png', upload_to=upload_to, blank=True, null=True)
    nome = models.CharField(max_length=100, help_text='Nome da empresa')
    cnpj = models.CharField(max_length=18, null=True, blank=True, help_text='CNPJ da empresa')
    qtd_funcionario = models.IntegerField(default=0, null=True, blank=True, help_text='Quantidade de funcionarios')
    
    def __str__(self):
        return self.nome

    def get_absolute_url(self):
        return reverse('index')