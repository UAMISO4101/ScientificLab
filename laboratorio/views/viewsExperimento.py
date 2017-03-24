import json
from django.http import JsonResponse
from django.core import serializers
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.exceptions import ValidationError, NotFound
from datetime import datetime
from ..models import Experimento, Proyecto, Responsable, Protocolo, ResultadoExperimento

#Atiende las peticiones de los Experimentos
@csrf_exempt
def experimentos(request):

    # Si es POST Graba
    if request.method == 'POST':
        data = json.loads(request.body)
        experimento = Experimento()
        if data.has_key("id"):
            experimento.id = data["id"]
        if data.has_key("nombre"):
            experimento.nombre = data["nombre"]
        if data.has_key("descripcion"):
            experimento.descripcion = data["descripcion"]
        if data.has_key("fechaInicio"):
            fechaInicioUnicode = data["fechaInicio"]
            experimento.fechaInicio = None
            if fechaInicioUnicode is not None:
                experimento.fechaInicio = datetime.strptime(fechaInicioUnicode, '%Y-%m-%d')
        if data.has_key("prioridad"):
            experimento.prioridad = data["prioridad"]
        if data.has_key("estado"):
            experimento.estado = data["estado"]
        if data.has_key("resultado"):
            experimento.resultado = data["resultado"]
        if data.has_key("idProyecto"):
            idProyecto = data["idProyecto"]
            try:
                proyecto = Proyecto.objects.get(id=idProyecto)
            except:
                raise ValidationError({'idProyecto': ['No existe proyecto ' + idProyecto]})
            experimento.proyecto = proyecto
        if data.has_key("idResponsable"):
            idResponsable = data["idResponsable"]
            try:
                responsable = Responsable.objects.get(id=idResponsable)
            except:
                raise ValidationError({'idResponsable': ['No existe responsable ' + idResponsable]})
            experimento.responsable = responsable
        experimento.save()
        return HttpResponse(serializers.serialize("json", [experimento]), content_type="application/json")
    # Si es GET Lista
    elif request.method == 'GET':
        experimentos = Experimento.objects.all()
        return HttpResponse(serializers.serialize("json", experimentos), content_type="application/json")
    else:
        raise NotFound(detail="No se encuentra comando rest experimentos con metodo " + request.method)

#Atiende las peticiones de un Experimento determinado
@csrf_exempt
def experimentos_id(request, id):

    # Si es DELETE Borra
    if request.method == 'DELETE':
        try:
            experimento = Experimento.objects.get(id=id)
        except:
            raise ValidationError({'id': ['No existe experimento ' + id]})
        experimento.delete()
        return JsonResponse({"Mensaje":"Experimento " + id + " borrado"})
    # Si es PUT Actualiza
    elif request.method == 'PUT':
        try:
            experimento = Experimento.objects.get(id=id)
        except:
            raise ValidationError({'id': ['No existe experimento ' + id]})
        data = json.loads(request.body)
        algoCambio = False
        if data.has_key("nombre"):
            experimento.nombre = data["nombre"]
            algoCambio = True
        if data.has_key("descripcion"):
            experimento.descripcion = data["descripcion"]
            algoCambio = True
        if data.has_key("fechaInicio"):
            fechaInicioUnicode = data["fechaInicio"]
            experimento.fechaInicio = None
            if fechaInicioUnicode is not None:
                experimento.fechaInicio = datetime.strptime(fechaInicioUnicode, '%Y-%m-%d')
            algoCambio = True
        if data.has_key("prioridad"):
            experimento.prioridad = data["prioridad"]
            algoCambio = True
        if data.has_key("estado"):
            experimento.estado = data["estado"]
            algoCambio = True
        if data.has_key("resultado"):
            experimento.resultado = data["resultado"]
            algoCambio = True
        if data.has_key("idProyecto"):
            idProyecto = data["idProyecto"]
            algoCambio = True
            try:
                proyecto = Proyecto.objects.get(id=idProyecto)
            except:
                raise ValidationError({'idProyecto': ['No existe proyecto ' + idProyecto]})
            experimento.proyecto = proyecto
        if data.has_key("idResponsable"):
            idResponsable = data["idResponsable"]
            algoCambio = True
            try:
                responsable = Responsable.objects.get(id=idResponsable)
            except:
                raise ValidationError({'idResponsable': ['No existe responsable ' + idResponsable]})
            experimento.responsable = responsable
        if algoCambio:
            experimento.save()
        return HttpResponse(serializers.serialize("json", [experimento]), content_type="application/json")
    # Si es GET Lista
    elif request.method == 'GET':
        try:
            experimento = Experimento.objects.get(id=id)
        except:
            raise ValidationError({'id': ['No existe experimento ' + id]})
        return HttpResponse(serializers.serialize("json", [experimento]), content_type="application/json")
    else:
        raise NotFound(detail="No se encuentra comando rest experimentos/{id} con metodo " + request.method)

#Atiende las peticiones de un Experimento determinado
@csrf_exempt
def experimentos_id_protocolos(request, id):
    # Si es GET Lista
    if request.method == 'GET':
        try:
            experimento = Experimento.objects.get(id=id)
        except:
            raise ValidationError({'id': ['No existe experimento ' + id]})
        protocolos = experimento.protocolo_set.all()
        return HttpResponse(serializers.serialize("json", protocolos), content_type="application/json")
    else:
        raise NotFound(detail="No se encuentra comando rest experimentos/{id}/protocolos con metodo " + request.method)
    
#Atiende las peticiones de Resultados de Experimento
@csrf_exempt
def lista_resultados_experimento(request):
    # Si es GET Lista
    if request.method == 'GET':
        try:
            resultados = ResultadoExperimento().getDict()
            print resultados
        except:
            raise ValidationError({'id': ['No fue posible generar la lista de resultados de experimento']})
        return HttpResponse(json.dumps(resultados), content_type="application/json")
    else:
        raise NotFound(detail="No se encuentra comando rest resultadosexperimento/ con metodo " + request.method)
