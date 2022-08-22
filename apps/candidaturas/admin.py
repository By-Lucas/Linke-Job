from django.contrib import admin

from candidaturas.models.models_qtd_candidaturas import QuatidadeCandidatura
from candidaturas.models.models_candidato import Candidatura, RequisitosCandidatura, EscolaridadeCandidatura

class CandidatosAdmin(admin.ModelAdmin):
    model = Candidatura
    list_display = ['caditatos', 'data_cadastro']
    
    # @staticmethod
    # def empresa(obj):
    #     return obj.vaga.empresa
    
    @staticmethod
    def caditatos(obj):
        return f'{obj.candidato} : {obj.codigo}'
    
admin.site.register(Candidatura, CandidatosAdmin)

admin.site.register(QuatidadeCandidatura)
admin.site.register(RequisitosCandidatura)
admin.site.register(EscolaridadeCandidatura)