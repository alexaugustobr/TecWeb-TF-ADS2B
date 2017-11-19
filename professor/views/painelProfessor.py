from django.shortcuts import render
from django.contrib.auth.decorators import login_required, user_passes_test

@login_required(login_url='/login')
@user_passes_test(lambda user: user.perfil == 'P', login_url='/login?error=acesso', redirect_field_name=None)
def painelProfessor (request):
    return render(request,"painel/painelProfessor.html")