from django.urls import path
from candidaturas.views.views_candidatura import CandidaturaDetailView

urlpatterns = [
    path('minhas-candidaturas/', CandidaturaDetailView.as_view(), name='CandidaturaDetailView'),
]