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
        protocolo = Protocolo.objects.get(id=idProtocolo)
        if protocolo is None:
            raise ValidationError({'idProtocolo': ['No existe este protocolo']})
        idExperimento = data["idExperimento"]
        experimento = Experimento.objects.get(id=idExperimento)
        if experimento is None:
            raise ValidationError({'idExperimento': ['No existe este experimento']})
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
        protocoloExperimento = ProtocolosExperimento.objects.get(id=id)
        protocoloExperimento.delete()
        return JsonResponse({"Mensaje":"ProtocoloExperimento " + id + " borrado"})
    # Si es PUT Actualiza
    elif request.method == 'PUT':
        protocoloExperimento = ProtocolosExperimento.objects.get(id=id)
        data = json.loads(request.body)
        algoCambio = False
        if data.has_key("idProtocolo"):
            idProtocolo = data["idProtocolo"]
            algoCambio = True
            protocolo = Protocolo.objects.get(id=idProtocolo)
            if protocolo is None:
                raise ValidationError({'idProtocolo': ['No existe este protocolo']})
            protocoloExperimento.protocolo = protocolo
        if data.has_key("idExperimento"):
            idExperimento = data["idExperimento"]
            algoCambio = True
            experimento = Experimento.objects.get(id=idExperimento)
            if experimento is None:
                raise ValidationError({'idExperimento': ['No existe este experimento']})
                protocoloExperimento.experimento = experimento
        if algoCambio:
            protocoloExperimento.save()
        return HttpResponse(serializers.serialize("json", [protocoloExperimento]))
    # Si es GET Lista
    elif request.method == 'GET':
        protocoloExperimento = ProtocolosExperimento.objects.get(id=id)
        return HttpResponse(serializers.serialize("json", [protocoloExperimento]))
    else:
        raise NotFound(detail="No se encuentra comando rest protocolosExperimento con metodo " + request.method)