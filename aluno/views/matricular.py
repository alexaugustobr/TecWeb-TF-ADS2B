from django.shortcuts import render
from django.http import HttpResponse
from core.components import *
def matricular (request):
    return render(request,"matricula/formMatricula.html")

def confirmar (request):



    return render(request,"matricula/formMatricula.html")
