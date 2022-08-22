from django import forms
from vagas.models.models_vagas import Vagas, RequisitosVaga


class CreateVagasForm(forms.ModelForm):
    class Meta:
        model = Vagas
        fields = [
        'empresa', 'criado_por', 'senioridade', 'tipo', 'nome', 'faixa_salarial',
        'requisitos', 'requisitos_adicionais', 'escolaridade', 
        'status', 'image'
    ]
        
    requisitos_adicionais = forms.ModelMultipleChoiceField(
        queryset=RequisitosVaga.objects.all(),
        widget=forms.CheckboxSelectMultiple
    )
    
class RequisitoForm(forms.ModelForm):
    class Meta:
        model = RequisitosVaga
        fields = ['nome']