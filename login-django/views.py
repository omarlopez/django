from django.shortcuts import render, render_to_response, redirect
from django.template import RequestContext
from login_django.forms import loginForm
from django.contrib.auth import authenticate, login, logout
# Create your views here.


def login_page(request):
    message = None 
    if request.method == 'POST':
        form = loginForm(request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']

            user = authenticate(username = username, password = password)

            if user is not None:
                if user.is_active:
                    login(request, user)
                    message =  " Te has identificado de modo correcto"
                else:
                    message = " Tu usuario esta inactivo"
            else:
                message = "Nombre de usuario y/o password incorrecto"
    else:
        form = loginForm()
    return render_to_response('login.html', {'message': message, 'form': form}, context_instance = RequestContext(request))

def homepage(request):
    return render_to_response('homepage.html', context_instance =RequestContext(request))

def logout_view(request):
    logout(request)
    return redirect('homepage')
