from django.urls import path
from .views.views_todas_vagas import VagasList, VagaDetailView

urlpatterns = [
    path("todas/", VagasList.as_view(), name='todas_vagas'),
    path('vaga/<int:pk>', VagaDetailView.as_view(), name='VagaDetailView'),
]
