import json
from django.http import JsonResponse
from django.core import serializers
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.exceptions import ValidationError, NotFound
from datetime import datetime
from ..models import Experimento, Proyecto, Responsable

#Atiende las peticiones de los Experimentos
@csrf_exempt
def experimentos(request):

    # Si es POST Graba
    if request.method == 'POST':
        data = json.loads(request.body)

        nombre = data["nombre"]
        descripcion = data["descripcion"]
        fechaInicioUnicode = data["fechaInicio"]
        fechaInicio = None
        if fechaInicioUnicode is not None:
            fechaInicio = datetime.strptime(fechaInicioUnicode, '%Y-%m-%d')
        prioridad = data["prioridad"]
        estado = data["estado"]
        resultado = data["resultado"]
        idProyecto = data["idProyecto"]
        proyecto = Proyecto.objects.get(id=idProyecto)
        if proyecto is None:
            raise ValidationError({'idProyecto': ['No existe proyecto' + idProyecto]})
        idResponsable = data["idResponsable"]
        responsable = Responsable.objects.get(id=idResponsable)
        if responsable is None:
            raise ValidationError({'idResponsable': ['No existe responsable' + idResponsable]})
        experimento = Experimento(nombre=nombre, descripcion=descripcion, fechaInicio=fechaInicio, prioridad=prioridad,
                                  estado=estado, resultado=resultado, proyecto=proyecto, responsable=responsable)
        experimento.save()
        return HttpResponse(serializers.serialize("json", [experimento]))
    # Si es GET Lista
    elif request.method == 'GET':
        experimentos = Experimento.objects.all()
        return HttpResponse(serializers.serialize("json", experimentos))
    else:
        raise NotFound(detail="No se encuentra comando rest experimentos con metodo " + request.method)

#Atiende las peticiones de un Experimento determinado
@csrf_exempt
def experimentos_id(request, id):

    # Si es DELETE Borra
    if request.method == 'DELETE':
        experimento = Experimento.objects.get(id=id)
        experimento.delete()
        return JsonResponse({"Mensaje":"Experimento " + id + " borrado"})
    # Si es PUT Actualiza
    elif request.method == 'PUT':
        experimento = Experimento.objects.get(id=id)
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
            proyecto = Proyecto.objects.get(id=idProyecto)
            if proyecto is None:
                raise ValidationError({'idProyecto': ['No existe proyecto ' + idProyecto]})
            experimento.proyecto = proyecto
        if data.has_key("idResponsable"):
            idResponsable = data["idResponsable"]
            algoCambio = True
            responsable = Responsable.objects.get(id=idResponsable)
            if responsable is None:
                raise ValidationError({'idResponsable': ['No existe responsable ' + idResponsable]})
            experimento.responsable = responsable
        if algoCambio:
            experimento.save()
        return HttpResponse(serializers.serialize("json", [experimento]))
    # Si es GET Lista
    elif request.method == 'GET':
        experimento = Experimento.objects.get(id=id)
        return HttpResponse(serializers.serialize("json", [experimento]))
    else:
        raise NotFound(detail="No se encuentra comando rest experimentos con metodo " + request.method)