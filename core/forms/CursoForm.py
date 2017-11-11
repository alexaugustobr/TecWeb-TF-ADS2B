from django import forms
from core.models import *

class ContatoForm(forms.Form):
    nome = forms.CharField()
    email = forms.EmailField()
    mensagem = forms.CharField()

    def envia_email(self):
        print("Email para você: \n"+
              "Aluno: " + self.cleaned_data["nome"]  + "\n"+
              "Email: " + self.cleaned_data["email"] + "\n"+
              "Mensagem: " + self.cleaned_data["mensagem"]
        )
