from django import forms

class QuestaoForm(forms.Form):
    turma_id = forms.IntegerField()
    descricao = forms.CharField()
    data_limite = forms.DateField()
    numero = forms.IntegerField()
    data = forms.DateField()