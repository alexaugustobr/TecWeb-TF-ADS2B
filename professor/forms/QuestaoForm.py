from django import forms
from core.models import ArquivosQuestao

class QuestaoForm(forms.Form):
    turma_id = forms.IntegerField()
    descricao = forms.CharField()
    arquivo = forms.FileField()
    data_limite = forms.DateField()
    numero = forms.IntegerField()
    data = forms.DateField()