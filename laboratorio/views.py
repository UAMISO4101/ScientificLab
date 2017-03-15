import json

from django.http import JsonResponse
from django.shortcuts import render
from django.http import HttpResponse
from django.core import serializers
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, render_to_response
from django.template import RequestContext
from django.views.decorators.csrf import csrf_exempt
from rest_framework.exceptions import ValidationError, NotFound
from models import Patrocinador, Proyecto
from datetime import datetime

# Create your views here.
def index(request):
    context = {'mensaje': 'Hola Mundo'}
    return render(request, 'laboratorio/index.html', context)
    #return HttpResponse("Hello, world. You're at the polls index.")

#Atiende las peticiones de los Patrocinadores
@csrf_exempt
def patrocinadores(request):

    # Si es POST Graba
    if request.method == 'POST':
        data = json.loads(request.body)
        nombre = data["nombre"]
        patrocinador = Patrocinador(nombre=nombre)
        patrocinador.save()
        return HttpResponse(serializers.serialize("json", [patrocinador]))
    # Si es GET Lista
    elif request.method == 'GET':
        patrocinadores = Patrocinador.objects.all()
        return HttpResponse(serializers.serialize("json", patrocinadores))
    else:
        raise NotFound(detail="No se encuentra comando rest patrocinadores con metodo " + request.method)

#Atiende las peticiones de un Patrocinador determinado
@csrf_exempt
def patrocinadores_id(request, id):

    # Si es DELETE Borra
    if request.method == 'DELETE':
        patrocinador = Patrocinador.objects.get(id=id)
        patrocinador.delete()
        return JsonResponse({"Mensaje":"Patrocinador " + id + " borrado"})
    # Si es PUT Actualiza
    elif request.method == 'PUT':
        patrocinador = Patrocinador.objects.get(id=id)
        data = json.loads(request.body)
        patrocinador.nombre = data["nombre"]
        patrocinador.save()
        return HttpResponse(serializers.serialize("json", [patrocinador]))
    # Si es GET Lista
    elif request.method == 'GET':
        patrocinador = Patrocinador.objects.get(id=id)
        return HttpResponse(serializers.serialize("json", [patrocinador]))
    else:
        raise NotFound(detail="No se encuentra comando rest patrocinadores con metodo " + request.method)


#Atiende las peticiones de los Proyectos
@csrf_exempt
def proyectos(request):

    # Si es POST Graba
    if request.method == 'POST':
        data = json.loads(request.body)
        nombre = data["nombre"]
        descripcion = data["descripcion"]
        fechaInicioUnicode = data["fechaInicio"]
        fechaInicio = None
        if fechaInicioUnicode is not None:
            fechaInicio = datetime.strptime(fechaInicioUnicode, '%Y-%m-%d')
        fechaFinalUnicode = data["fechaFinal"]
        fechaFinal = None
        if fechaFinalUnicode is not None:
            fechaFinal = datetime.strptime(fechaFinalUnicode, '%Y-%m-%d')
        prioridad = data["prioridad"]
        avance = data["avance"]
        estado = data["estado"]
        idPatrocinador = data["idPatrocinador"]
        patrocinador = Patrocinador.objects.get(id=idPatrocinador)
        if patrocinador is None:
            raise ValidationError({'idPatrocinador': ['No existe este patrocinador']})
        proyecto = Proyecto(nombre=nombre, descripcion=descripcion, fechaInicio=fechaInicio, fechaFinal=fechaFinal,
                            prioridad=prioridad, avance=avance, estado=estado, patrocinador=patrocinador)
        proyecto.save()
        return HttpResponse(serializers.serialize("json", [proyecto]))
    # Si es GET Lista
    elif request.method == 'GET':
        proyectos = Proyecto.objects.all()
        return HttpResponse(serializers.serialize("json", proyectos))
    else:
        raise NotFound(detail="No se encuentra comando rest proyectos con metodo " + request.method)

#Atiende las peticiones de un Proyecto determinado
@csrf_exempt
def proyectos_id(request, id):

    # Si es DELETE Borra
    if request.method == 'DELETE':
        proyecto = Proyecto.objects.get(id=id)
        proyecto.delete()
        return JsonResponse({"Mensaje":"Proyecto " + id + " borrado"})
    # Si es PUT Actualiza
    elif request.method == 'PUT':
        proyecto = Proyecto.objects.get(id=id)
        data = json.loads(request.body)
        proyecto.nombre = data["nombre"]

        proyecto.nombre = data["nombre"]
        proyecto.descripcion = data["descripcion"]
        fechaInicioUnicode = data["fechaInicio"]
        proyecto.fechaInicio = None
        if fechaInicioUnicode is not None:
            proyecto.fechaInicio = datetime.strptime(fechaInicioUnicode, '%Y-%m-%d')
        fechaFinalUnicode = data["fechaFinal"]
        proyecto.fechaFinal = None
        if fechaFinalUnicode is not None:
            proyecto.fechaFinal = datetime.strptime(fechaFinalUnicode, '%Y-%m-%d')
        proyecto.prioridad = data["prioridad"]
        proyecto.avance = data["avance"]
        proyecto.estado = data["estado"]
        idPatrocinador = data["idPatrocinador"]
        patrocinador = Patrocinador.objects.get(id=idPatrocinador)
        if patrocinador is None:
            raise ValidationError({'idPatrocinador': ['No existe este patrocinador']})
        proyecto.patrocinador = patrocinador
        proyecto.save()
        return HttpResponse(serializers.serialize("json", [proyecto]))
    # Si es GET Lista
    elif request.method == 'GET':
        proyecto = Proyecto.objects.get(id=id)
        return HttpResponse(serializers.serialize("json", [proyecto]))
    else:
        raise NotFound(detail="No se encuentra comando rest proyectos con metodo " + request.method)
