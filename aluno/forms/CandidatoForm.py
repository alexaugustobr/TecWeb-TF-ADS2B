from django import forms
from core.models import *
class CandidatoForm(forms.ModelForm):
    class Meta:
        model = Candidato
        fields = "__all__"
