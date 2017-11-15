from django.shortcuts import render

def matricular (request):
    return render(request,"matricula/formMatricula.html")