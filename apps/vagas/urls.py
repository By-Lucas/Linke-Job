from django.urls import path
from .views.views_todas_vagas import todas_vagas

urlpatterns = [
    path("todas/", todas_vagas, name='todas_vagas'),
]
