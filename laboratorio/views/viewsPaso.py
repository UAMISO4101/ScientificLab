import json
from django.http import JsonResponse
from django.core import serializers
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.exceptions import ValidationError, NotFound
from ..models import Paso, Protocolo

#Atiende las peticiones de los Pasos
@csrf_exempt
def pasos(request):

    # Si es POST Graba
    if request.method == 'POST':
        data = json.loads(request.body)
        nombre = data["nombre"]
        idProtocolo = data["idProtocolo"]
        protocolo = Protocolo.objects.get(id=idProtocolo)
        if protocolo is None:
            raise ValidationError({'idProtocolo': ['No existe protocolo ' + idProtocolo]})
        paso = Paso(nombre=nombre, protocolo=protocolo)
        paso.save()
        return HttpResponse(serializers.serialize("json", [paso]))
    # Si es GET Lista
    elif request.method == 'GET':
        pasos = Paso.objects.all()
        return HttpResponse(serializers.serialize("json", pasos))
    else:
        raise NotFound(detail="No se encuentra comando rest pasos con metodo " + request.method)

#Atiende las peticiones de un Paso determinado
@csrf_exempt
def pasos_id(request, id):

    # Si es DELETE Borra
    if request.method == 'DELETE':
        paso = Paso.objects.get(id=id)
        paso.delete()
        return JsonResponse({"Mensaje":"Paso " + id + " borrado"})
    # Si es PUT Actualiza
    elif request.method == 'PUT':
        paso = Paso.objects.get(id=id)
        data = json.loads(request.body)
        algoCambio = False
        if data.has_key("nombre"):
            paso.nombre = data["nombre"]
            algoCambio = True
        if data.has_key("idProtocolo"):
            idProtocolo = data["idProtocolo"]
            algoCambio = True
            protocolo = Protocolo.objects.get(id=idProtocolo)
            if protocolo is None:
                raise ValidationError({'idProtocolo': ['No existe protocolo ' + idProtocolo]})
            paso.protocolo = protocolo
        if algoCambio:
            paso.save()
        return HttpResponse(serializers.serialize("json", [paso]))
    # Si es GET Lista
    elif request.method == 'GET':
        paso = Paso.objects.get(id=id)
        return HttpResponse(serializers.serialize("json", [paso]))
    else:
        raise NotFound(detail="No se encuentra comando rest pasos con metodo " + request.method)