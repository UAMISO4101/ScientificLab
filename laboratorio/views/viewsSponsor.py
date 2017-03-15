import json
from django.http import JsonResponse
from django.core import serializers
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from ..models import Patrocinador


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
