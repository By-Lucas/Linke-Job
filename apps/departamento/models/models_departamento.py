from audioop import reverse
from django.db import models
from empresas.models.models_empresa import Empresa
from django.urls import reverse

class Departamento(models.Model):
    departamento = models.CharField(max_length=100, help_text="Nome do departamento")
    empresa = models.ForeignKey(Empresa, on_delete=models.PROTECT)

    # Apos o formulario ser validado, vai redirecionar para a pagina abaixo
    #def get_absolute_url(self):
    #    return reverse('list_departamento')

    def __str__(self):
        return self.departamento