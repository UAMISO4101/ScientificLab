import json
from django.http import JsonResponse
from django.core import serializers
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.exceptions import ValidationError, NotFound
from ..models import Protocolo

#Atiende las peticiones de los Protocolos
@csrf_exempt
def protocolos(request):

    # Si es POST Graba
    if request.method == 'POST':
        data = json.loads(request.body)
        titulo = data["titulo"]
        descripcion = data["descripcion"]
        version = data["version"]
        categoria = data["categoria"]
        protocolo = Protocolo(titulo=titulo, descripcion=descripcion, version=version, categoria=categoria)
        protocolo.save()
        return HttpResponse(serializers.serialize("json", [protocolo]))
    # Si es GET Lista
    elif request.method == 'GET':
        protocolos = Protocolo.objects.all()
        return HttpResponse(serializers.serialize("json", protocolos))
    else:
        raise NotFound(detail="No se encuentra comando rest protocolos con metodo " + request.method)

#Atiende las peticiones de un Protocolo determinado
@csrf_exempt
def protocolos_id(request, id):

    # Si es DELETE Borra
    if request.method == 'DELETE':
        try:
            protocolo = Protocolo.objects.get(id=id)
        except:
            raise ValidationError({'id': ['No existe protocolo ' + id]})
        protocolo.delete()
        return JsonResponse({"Mensaje":"Protocolo " + id + " borrado"})
    # Si es PUT Actualiza
    elif request.method == 'PUT':
        try:
            protocolo = Protocolo.objects.get(id=id)
        except:
            raise ValidationError({'id': ['No existe protocolo ' + id]})
        data = json.loads(request.body)
        algoCambio = False
        if data.has_key("titulo"):
            protocolo.titulo = data["titulo"]
            algoCambio = True
        if data.has_key("descripcion"):
            protocolo.descripcion = data["descripcion"]
            algoCambio = True
        if data.has_key("version"):
            protocolo.version = data["version"]
            algoCambio = True
        if data.has_key("categoria"):
            protocolo.categoria = data["categoria"]
            algoCambio = True
        if algoCambio:
            protocolo.save()
        return HttpResponse(serializers.serialize("json", [protocolo]))
    # Si es GET Lista
    elif request.method == 'GET':
        try:
            protocolo = Protocolo.objects.get(id=id)
        except:
            raise ValidationError({'id': ['No existe protocolo ' + id]})
        return HttpResponse(serializers.serialize("json", [protocolo]))
    else:
        raise NotFound(detail="No se encuentra comando rest protocolos con metodo " + request.method)