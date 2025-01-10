from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home.html')
def user(request):
    return render(request, 'user.html')

def blank(request):
    return render(request, 'blank.html')

from django.shortcuts import render, redirect


def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')  # Obtén el valor o devuelve None si no existe
        password = request.POST.get('password')  # Asegúrate de manejar la clave 'password'
        if username and password:
            # Lógica adicional de autenticación
            return redirect('user')  # Redirige al nombre de URL 'user'
        else:
            return HttpResponse("Por favor, proporciona un nombre de usuario y contraseña válidos.")
    return render(request, 'login.html')


def user_panel(request):
    return None

def login_view(request):
    return None