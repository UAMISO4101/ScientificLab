import json
from django.http import JsonResponse
from django.core import serializers
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.exceptions import ValidationError, NotFound
from ..models import ProtocolosExperimento, Protocolo, Experimento
from django.shortcuts import render
from rest_framework import generics
from ..serializers import ProtocolosExperimentoSerealizer

class ProtocolosExperimentoLista(generics.ListAPIView):
    serializer_class = ProtocolosExperimentoSerealizer
    def get_queryset(self):
        experimento = self.request.query_params.get('experimento')
        if(experimento !=0 ):
            protocolosexperimentos = ProtocolosExperimento.objects.filter(experimento_id=experimento)
        else:
            protocolosexperimentos = ProtocolosExperimento.objects.all()
        return protocolosexperimentos

def agregar_expeprotocolo(request, id):
    return render(request, 'laboratorio/Experimento/agregarExperimentoProtocolo.html',
                  {"experimento": Experimento.objects.get(id=id)})

#Atiende las peticiones de los ProtocolosExperimento
@csrf_exempt
def protocolosExperimento(request):

    if request.method == 'POST':
        data = json.loads(request.body)
        protocoloExperimento = ProtocolosExperimento()
        if data.has_key("id"):
            protocoloExperimento.id = data["id"]
        if data.has_key("idProtocolo"):
            idProtocolo = data["idProtocolo"]
            try:
                protocolo = Protocolo.objects.get(id=idProtocolo)
            except:
                raise ValidationError({'idProtocolo': ['No existe protocolo ' + idProtocolo]})
            protocoloExperimento.protocolo = protocolo
        if data.has_key("idExperimento"):
            idExperimento = data["idExperimento"]
            try:
                experimento = Experimento.objects.get(id=idExperimento)
            except:
                raise ValidationError({'idExperimento': ['No existe experimento ' + idExperimento]})
            protocoloExperimento.experimento = experimento
        protocoloExperimento.save()
        return HttpResponse(serializers.serialize("json", [protocoloExperimento]), content_type="application/json")

    elif request.method == 'GET':
        protocolosExperimento = ProtocolosExperimento.objects.all()
        return HttpResponse(serializers.serialize("json", protocolosExperimento), content_type="application/json")
    else:
        raise NotFound(detail="No se encuentra comando rest protocolosExperimento con metodo " + request.method)

#Atiende las peticiones de un ProtocoloExperimento determinado
@csrf_exempt
def protocolosExperimento_id(request, id):

    if request.method == 'DELETE':
        try:
            protocoloExperimento = ProtocolosExperimento.objects.get(id=id)
        except:
            raise ValidationError({'id': ['No existe Protocolo Experimento ' + id]})
        protocoloExperimento.delete()
        return JsonResponse({"Mensaje":"ProtocoloExperimento " + id + " borrado"})

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
        return HttpResponse(serializers.serialize("json", [protocoloExperimento]), content_type="application/json")

    elif request.method == 'GET':
        try:
            protocoloExperimento = ProtocolosExperimento.objects.get(id=id)
        except:
            raise ValidationError({'id': ['No existe Protocolo Experimento ' + id]})
        return HttpResponse(serializers.serialize("json", [protocoloExperimento]), content_type="application/json")
    else:
        raise NotFound(detail="No se encuentra comando rest protocolosExperimento/{id} con metodo " + request.method)

