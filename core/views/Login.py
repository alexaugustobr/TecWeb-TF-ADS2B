from django.shortcuts import render

def loginHome (request):
    return render(request,"login/login.html")
def esqueciSenha (request):
    return render(request,"login/esqueciSenha.html")