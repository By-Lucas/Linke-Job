from import_export import resources
from .models.models_candidaturas import Candidaturas

class Candidaturas_Resource(resources.ModelResource):
    class Meta:
        model = Candidaturas
        fields = ['candidatos', 'vaga']