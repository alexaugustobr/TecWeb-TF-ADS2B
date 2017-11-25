from django.shortcuts import render
from core.models.Curso import Curso


def cursos (request):
    contexto = {
        'cursos': Curso.objects.all(),
    }
    return render(request,"cursos/cursos.html",contexto)

def cursosListar (request):
    
    contexto = {
        "usuario":"usuario",
        "cursos":Curso.objects.all()
    }
    return render(request,"cursos/cursos.html")


def bancoDados (request):
    return render(request,"cursos/cursoBancoDados.html")

def detalheCurso (request, sigla):
    
    contexto = {
        "curso":Curso.objects.get(sigla=sigla)
    }
    return render(request,"cursos/detalheCurso.html", contexto)