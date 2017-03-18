import json
from django.http import JsonResponse
from django.core import serializers
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.exceptions import ValidationError, NotFound
from ..models import ProtocolosExperimento, Protocolo, Experimento

#Atiende las peticiones de los ProtocolosExperimento
@csrf_exempt
def protocolosExperimento(request):

    # Si es POST Graba
    if request.method == 'POST':
        data = json.loads(request.body)
        idProtocolo = data["idProtocolo"]
        try:
            protocolo = Protocolo.objects.get(id=idProtocolo)
        except:
            raise ValidationError({'idProtocolo': ['No existe protocolo ' + idProtocolo]})
        idExperimento = data["idExperimento"]
        try:
            experimento = Experimento.objects.get(id=idExperimento)
        except:
            raise ValidationError({'idExperimento': ['No existe experimento ' + idExperimento]})
        protocoloExperimento = ProtocolosExperimento(protocolo=protocolo, experimento=experimento)
        protocoloExperimento.save()
        return HttpResponse(serializers.serialize("json", [protocoloExperimento]))
    # Si es GET Lista
    elif request.method == 'GET':
        protocolosExperimento = ProtocolosExperimento.objects.all()
        return HttpResponse(serializers.serialize("json", protocolosExperimento))
    else:
        raise NotFound(detail="No se encuentra comando rest protocolosExperimento con metodo " + request.method)

#Atiende las peticiones de un ProtocoloExperimento determinado
@csrf_exempt
def protocolosExperimento_id(request, id):

    # Si es DELETE Borra
    if request.method == 'DELETE':
        try:
            protocoloExperimento = ProtocolosExperimento.objects.get(id=id)
        except:
            raise ValidationError({'id': ['No existe Protocolo Experimento ' + id]})
        protocoloExperimento.delete()
        return JsonResponse({"Mensaje":"ProtocoloExperimento " + id + " borrado"})
    # Si es PUT Actualiza
    elif request.method == 'PUT':
        try:
            protocoloExperimento = ProtocolosExperimento.objects.get(id=id)
        except:
            raise ValidationError({'id': ['No existe Protocolo Experimento ' + id]})
        data = json.loads(request.body)
        algoCambio = False
        if data.has_key("idProtocolo"):
            idProtocolo = data["idProtocolo"]
            algoCambio = True
            try:
                protocolo = Protocolo.objects.get(id=idProtocolo)
            except:
                raise ValidationError({'idProtocolo': ['No existe protocolo ' + idProtocolo]})
            protocoloExperimento.protocolo = protocolo
        if data.has_key("idExperimento"):
            idExperimento = data["idExperimento"]
            algoCambio = True
            try:
                experimento = Experimento.objects.get(id=idExperimento)
            except:
                raise ValidationError({'idExperimento': ['No existe experimento ' + idExperimento]})
            protocoloExperimento.experimento = experimento
        if algoCambio:
            protocoloExperimento.save()
        return HttpResponse(serializers.serialize("json", [protocoloExperimento]))
    # Si es GET Lista
    elif request.method == 'GET':
        try:
            protocoloExperimento = ProtocolosExperimento.objects.get(id=id)
        except:
            raise ValidationError({'id': ['No existe Protocolo Experimento ' + id]})
        return HttpResponse(serializers.serialize("json", [protocoloExperimento]))
    else:
        raise NotFound(detail="No se encuentra comando rest protocolosExperimento con metodo " + request.method)