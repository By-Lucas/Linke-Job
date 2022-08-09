from django.db import models
from django.urls import reverse

class Empresa(models.Model):
    #user = models.ForeignKey()
    nome = models.CharField(max_length=100, help_text='Nome da empresa')

    def __str__(self):
        return self.nome

    #Direciona após salvar edição
    #def get_absolute_url(self):
    #    return reverse('home')