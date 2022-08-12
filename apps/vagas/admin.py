from django.contrib import admin
from .models.models_vagas import Vagas, RequisitosVaga, EscolaridadeVaga

admin.site.register(Vagas)
admin.site.register(RequisitosVaga)
admin.site.register(EscolaridadeVaga)