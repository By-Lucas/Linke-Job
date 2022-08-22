from django.shortcuts import render

from .models.moels_funcionario import Funcionario

# Create your views here.
class FuncionariosList(DetailView):
    model = Funcionario
    def get_queryset(self):
        empresa_logada = self.request.user.funcionario.empresa
        return Funcionario.objects.all(empresa=empresa_logada)