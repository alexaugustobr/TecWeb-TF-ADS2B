from django.shortcuts import render

def cursos (request):
    return render(request,"cursos/cursos.html")

def bancoDados (request):
    return render(request,"cursos/cursoBancoDados.html")

def detalheCurso (request):
    return render(request,"cursos/detalheCurso.html")