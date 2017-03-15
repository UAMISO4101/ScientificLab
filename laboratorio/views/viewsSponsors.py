import json
from django.http import JsonResponse
from django.core import serializers
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from ..models import Patrocinador

#Atiende las peticiones de los Patrocinadores
@csrf_exempt
def patrocinadores(request):

    # Si es POST Graba
    #if request.is_ajax():
    # #Falta pero no lo puedo determinar en la prueba que dato requiere para determinar si es una peticion ajax
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
        return JsonResponse({"Mensaje":"No entendi la peticion"})


#Atiende las peticiones de un Patrocinador determinado
@csrf_exempt
def patrocinadores(request, id):

    # Si es DELETE Borra
    #if request.is_ajax():
    # #Falta pero no lo puedo determinar en la prueba que dato requiere para determinar si es una peticion ajax
    if request.method == 'DELETE':
        patrocinador = Patrocinador.objects.get(id=id)
        patrocinador.delete()
        return JsonResponse({"Mensaje":"Patrocinador " + id + " borrado"})
    # Si es PUT Actualiza
    elif request.method == 'PUT':
        patrocinador = Patrocinador.objects.get(id=id)
        data = json.loads(request.body)
        print "Este es el nombre " + data["nombre"]
        patrocinador.nombre = data["nombre"]
        patrocinador.save()
        return HttpResponse(serializers.serialize("json", [patrocinador]))
    else:
        return JsonResponse({"Mensaje":"No entendi la peticion"})
