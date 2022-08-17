from tkinter import CASCADE
from django.db import models
from django.utils import timezone

from vagas.models.models_vagas import Vagas

class QuatidadeCandidatura(models.Model):
    #id = models.IntegerField(unique=False, editable=True, primary_key=True,  blank=True)
    vaga = models.CharField(max_length=70)
    quantidade_candidatos = models.IntegerField(default=0, null=True, blank=True)
    atualizado_em = models.DateTimeField(default=timezone.now)
    data_cadastro = models.DateTimeField(auto_now = True)

    def __str__(self):
        return f'Candidatos: {self.quantidade_candidatos} a vaga {self.vaga}'