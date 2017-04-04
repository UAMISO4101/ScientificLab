# -*- encoding: utf-8 -*-
# from django.contrib.auth import authenticate, login, logout
from django.contrib.auth import authenticate, login, logout
from django.core import serializers
from django.core.urlresolvers import reverse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.exceptions import NotFound

# Muestra la pagina de inicio de sesion
def inicio_sesion(request):
    return render(request, 'laboratorio/Usuario/login.html')

# Muestra la pagina de agregar usuario
def agregar_usuario(request):
    return render(request, 'laboratorio/Usuario/agregarUsuario.html')

# Inicia la sesion de usuario
@csrf_exempt
def iniciar_sesion(request):
    if request.method == 'POST':
        data = request.POST
        username = data['username']
        password = data['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            mensaje = 'ok'
        else:
            mensaje = 'Nombre de usuario o clave no valido'

    return JsonResponse({'mensaje': mensaje})

# Cierra la sesion iniciada por un usuario
@csrf_exempt
def cerrar_sesion(request):
    logout(request)
    return JsonResponse({'mensaje': 'ok'})

# Determina si un usuario ha iniciado sesión
@csrf_exempt
def esta_logueado(request):
    if request.user.is_authenticated():
        mensaje = request.user.first_name
    else:
        mensaje = 'no'

    return JsonResponse({'mensaje': mensaje})


# Atiende las peticiones de los Proyectos
@csrf_exempt
def usuarios(request):
    if request.method == 'POST':
        data = request.POST
        user_model = User.objects.create_user(username=data["username"], password=data["password"])
        user_model.first_name = data["first_name"]
        user_model.last_name = data["last_name"]
        user_model.email = data["email"]
        user_model.save()

        return HttpResponse(serializers.serialize("json", [user_model]))
    else:
        raise NotFound(detail="No se encuentra comando rest usuarios/ con metodo " + request.method)
