from django.contrib import admin
from .models.models_vagas import Vagas, RequisitosVaga, EscolaridadeVaga
from .models.candidaturas_vaga import QtdCandidatura

admin.site.register(Vagas)
admin.site.register(RequisitosVaga)
admin.site.register(EscolaridadeVaga)
admin.site.register(QtdCandidatura)