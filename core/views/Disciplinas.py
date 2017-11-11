from django.shortcuts import render

def disciplinasNovo (request):
    return render(request,"disciplinas/disciplinasNovo.html")