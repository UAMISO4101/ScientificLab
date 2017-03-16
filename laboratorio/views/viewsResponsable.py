import json
from django.http import JsonResponse
from django.core import serializers
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.exceptions import NotFound
from ..models import Responsable

#Atiende las peticiones de los Responsables
@csrf_exempt
def responsables(request):

    # Si es POST Graba
    if request.method == 'POST':
        data = json.loads(request.body)
        nombre = data["nombre"]
        responsable = Responsable(nombre=nombre)
        responsable.save()
        return HttpResponse(serializers.serialize("json", [responsable]))
    # Si es GET Lista
    elif request.method == 'GET':
        responsables = Responsable.objects.all()
        return HttpResponse(serializers.serialize("json", responsables))
    else:
        raise NotFound(detail="No se encuentra comando rest responsables con metodo " + request.method)

#Atiende las peticiones de un Responsable determinado
@csrf_exempt
def responsables_id(request, id):

    # Si es DELETE Borra
    if request.method == 'DELETE':
        responsable = Responsable.objects.get(id=id)
        responsable.delete()
        return JsonResponse({"Mensaje":"Responsable " + id + " borrado"})
    # Si es PUT Actualiza
    elif request.method == 'PUT':
        responsable = Responsable.objects.get(id=id)
        data = json.loads(request.body)
        algoCambio = False
        if data.has_key("nombre"):
            responsable.nombre = data["nombre"]
            algoCambio = True
        if algoCambio:
            responsable.save()
        return HttpResponse(serializers.serialize("json", [responsable]))
    # Si es GET Lista
    elif request.method == 'GET':
        responsable = Responsable.objects.get(id=id)
        return HttpResponse(serializers.serialize("json", [responsable]))
    else:
        raise NotFound(detail="No se encuentra comando rest responsables con metodo " + request.method)
