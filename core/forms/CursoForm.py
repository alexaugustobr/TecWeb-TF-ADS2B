from django import forms
from core.models import *

class CursoForm(forms.ModelForm):
    class Meta:
        model = Curso
        fields = "__all__"
