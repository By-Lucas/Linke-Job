from django.urls import path
from .views.views_todas_vagas import VagasList

urlpatterns = [
    path("todas/", VagasList.as_view(), name='todas_vagas'),
]
