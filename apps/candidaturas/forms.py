from django import forms
from candidaturas.models.models_candidato import Candidatura, RequisitosCandidatura, EscolaridadeCandidatura


class CandidaturaForm(forms.ModelForm):
    # requisitos_adicionais = forms.Modelmultiplechoicefield (label ='Requisitos adicionais',
    #                                         widget=forms.CheckboxSelectMultiple,
    #                                         queryset=RequisitosCandidatura.objects.filter(enable=True))
    # escolaridade = forms.Modelmultiplechoicefield (label ='Escolaridade',
    #                                         widget=forms.CheckboxSelectMultiple,
    #                                         queryset=EscolaridadeCandidatura.objects.filter(enable=True))
    
    class Meta:
        model = Candidatura
        fields = ['candidato', 'vaga', 'requisitos' ] #'requisitos_adicionais', 'escolaridade'