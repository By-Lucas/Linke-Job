from django.contrib import admin

from .models.models_candidato import Candidatura

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