from django.shortcuts import render

def noticias (request):
    return render(request,"noticias/noticias.html")

def detalheNoticia(request):
    return render(request,"noticias/detalheNoticia.html")

def detalheNoticia2(request):
    return render(request,"noticias/detalheNoticia2.html")