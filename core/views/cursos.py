from django.shortcuts import render
from core.models.Curso import Curso

def cursos (request):

    contexto = {
        "usuario":"usuario",
        "cursos":Curso.objects.all()
    }
    return render(request,"cursos/cursos.html",contexto)

def bancoDados (request):
    return render(request,"cursos/cursoBancoDados.html")

def detalheCurso (request):
    return render(request,"cursos/detalheCurso.html")