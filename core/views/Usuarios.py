from django.shortcuts import render

def usuariosNovo (request):
    return render(request,"usuarios/usuariosNovo.html")