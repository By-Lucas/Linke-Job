from django.urls import path

from .views.views_todas_vagas import VagasList, VagaDetailView, pegar_dados
from vagas.views.views_acoes_vagas import CreateVaga, DeleteVaga, ListVagasOn, UpdateVaga

urlpatterns = [
    path("todas/", VagasList.as_view(), name='todas_vagas'),
    path('vaga/<int:pk>/', VagaDetailView.as_view(), name='VagaDetailView'),
    path('pegar/<int:id>/', pegar_dados, name='pegar_dados'),
    
    path('cadastrar-vaga/', CreateVaga.as_view(), name='CreateVaga'),
    path('minhas-vagas/', ListVagasOn.as_view(), name='ListVagasOn'),
    path('delete/<int:pk>/', DeleteVaga.as_view(), name='DeleteVaga'),
    path('atualizar/<int:pk>/', UpdateVaga.as_view(), name='UpdateVaga'),
]
