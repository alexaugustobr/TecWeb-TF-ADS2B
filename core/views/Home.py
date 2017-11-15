from django.shortcuts import render
from core.models.Curso import Curso
def index (request):
    contexto = {
        'cursos': Curso.objects.all(),
    }
    return render(request,"home/index.html",contexto)