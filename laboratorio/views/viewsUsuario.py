# -*- encoding: utf-8 -*-
import json
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render
from django.contrib.auth.models import User
from ..models import Proyecto, Experimento
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.exceptions import NotFound, ValidationError
from rest_framework.renderers import JSONRenderer
from rest_framework import generics
from ..serializers import ResponsableSerializer, UserSerializer, ResponsablesXProyectoSerializer


# Consulta de usuarios
class UsuariosLista(generics.ListAPIView):
    serializer_class = ResponsableSerializer
    def get_queryset(self):
        name = self.request.query_params.get('name')
        idUser= self.request.query_params.get('id')
        listResponsables = set()
        if(idUser):
           for Resp in Experimento.objects.filter(proyecto_id=idUser).select_related('responsable'):
               listResponsables.add(Resp.responsable)
        elif(name):
           for Resp in Experimento.objects.filter(proyecto_id=idUser).select_related('responsable').filter(nombre__icontains=name):
               listResponsables.add(Resp.responsable)
        return listResponsables


class UsuariosProyecto(generics.ListAPIView):
    serializer_class = ResponsablesXProyectoSerializer
    #Trazabilidad: Participantes
    def get_queryset(self):
        id = self.request.query_params.get('id')
        listResponsables = list()
        if (id):
            for Resp in Experimento.objects.filter(proyecto_id=id).select_related('responsable'):
                    listResponsables.append(Resp.responsable)
        return listResponsables


def listar_usuariosProyecto(request, id):
    project = Proyecto.objects.get(id=id)
    return render(request, 'laboratorio/Usuario/usuariosProyecto.html', {'projectId': id, 'projectName':project.nombre})

# Muestra la pagina para inicio de sesion (login)
def inicio_sesion(request):
    return render(request, 'laboratorio/Usuario/login.html')

# Muestra la pagina de agregar usuario
def agregar_usuario(request):
    return render(request, 'laboratorio/Usuario/agregarUsuario.html')

# Inicia la sesion de usuario
@csrf_exempt
def iniciar_sesion(request):
    if request.method == 'POST':
        data = json.loads(request.body)
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
        data = json.loads(request.body)
        usuario = User.objects.create_user(username=data["username"], password=data["password"])
        usuario.first_name = data["first_name"]
        usuario.last_name = data["last_name"]
        usuario.email = data["email"]
        usuario.save()

        serializer = UserSerializer(usuario)
        return HttpResponse(JSONRenderer().render(serializer.data), content_type="application/json")
    elif request.method == 'GET':
        usuarios = User.objects.all()
        serializer = UserSerializer(usuarios, many=True)
        return HttpResponse(JSONRenderer().render(serializer.data), content_type="application/json")
    else:
        raise NotFound(detail="No se encuentra comando rest usuarios con metodo " + request.method)


#Atiende las peticiones de un Usuario determinado
@csrf_exempt
def usuarios_id(request, id):

    if request.method == 'DELETE':
        try:
            usuario = User.objects.get(id=id)
        except:
            raise ValidationError({'id': ['No existe usuario ' + id]})
        usuario.delete()
        return JsonResponse({"Mensaje":"Usuario " + id + " borrado"})

    elif request.method == 'PUT':
        try:
            usuario = User.objects.get(id=id)
        except:
            raise ValidationError({'id': ['No existe usuario ' + id]})
        data = json.loads(request.body)
        algoCambio = False
        if data.has_key("username"):
            usuario.username = data["username"]
            algoCambio = True
        if data.has_key("password"):
            usuario.password = data["password"]
            algoCambio = True
        if data.has_key("first_name"):
            usuario.first_name = data["first_name"]
            algoCambio = True
        if data.has_key("last_name"):
            usuario.last_name = data["last_name"]
            algoCambio = True
        if data.has_key("email"):
            usuario.email = data["email"]
            algoCambio = True
        if algoCambio:
            usuario.save()
        serializer = UserSerializer(usuario)
        return HttpResponse(JSONRenderer().render(serializer.data), content_type="application/json")

    elif request.method == 'GET':
        try:
            usuario = User.objects.get(id=id)
        except:
            raise ValidationError({'id': ['No existe usuario ' + id]})
        serializer = UserSerializer(usuario)
        return HttpResponse(JSONRenderer().render(serializer.data), content_type="application/json")
    else:
        raise NotFound(detail="No se encuentra comando rest usuarios/{id} con metodo " + request.method)

