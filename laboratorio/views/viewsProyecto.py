import json
from django.http import JsonResponse
from django.core import serializers
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.exceptions import ValidationError, NotFound
from datetime import datetime
from ..models import Proyecto, Patrocinador

#Atiende las peticiones de los Proyectos
@csrf_exempt
def proyectos(request):

    # Si es POST Graba
    if request.method == 'POST':
        data = json.loads(request.body)
        nombre = data["nombre"]
        descripcion = data["descripcion"]
        fechaInicioUnicode = data["fechaInicio"]
        fechaInicio = None
        if fechaInicioUnicode is not None:
            fechaInicio = datetime.strptime(fechaInicioUnicode, '%Y-%m-%d')
        fechaFinalUnicode = data["fechaFinal"]
        fechaFinal = None
        if fechaFinalUnicode is not None:
            fechaFinal = datetime.strptime(fechaFinalUnicode, '%Y-%m-%d')
        prioridad = data["prioridad"]
        avance = data["avance"]
        estado = data["estado"]
        idPatrocinador = data["idPatrocinador"]
        patrocinador = Patrocinador.objects.get(id=idPatrocinador)
        if patrocinador is None:
            raise ValidationError({'idPatrocinador': ['No existe este patrocinador']})
        proyecto = Proyecto(nombre=nombre, descripcion=descripcion, fechaInicio=fechaInicio, fechaFinal=fechaFinal,
                            prioridad=prioridad, avance=avance, estado=estado, patrocinador=patrocinador)
        proyecto.save()
        return HttpResponse(serializers.serialize("json", [proyecto]))
    # Si es GET Lista
    elif request.method == 'GET':
        proyectos = Proyecto.objects.all()
        return HttpResponse(serializers.serialize("json", proyectos))
    else:
        raise NotFound(detail="No se encuentra comando rest proyectos con metodo " + request.method)

#Atiende las peticiones de un Proyecto determinado
@csrf_exempt
def proyectos_id(request, id):

    # Si es DELETE Borra
    if request.method == 'DELETE':
        proyecto = Proyecto.objects.get(id=id)
        proyecto.delete()
        return JsonResponse({"Mensaje":"Proyecto " + id + " borrado"})
    # Si es PUT Actualiza
    elif request.method == 'PUT':
        proyecto = Proyecto.objects.get(id=id)
        data = json.loads(request.body)
        algoCambio = False
        if data.has_key("nombre"):
            proyecto.nombre = data["nombre"]
            algoCambio = True
        if data.has_key("descripcion"):
            proyecto.descripcion = data["descripcion"]
            algoCambio = True
        if data.has_key("fechaInicio"):
            fechaInicioUnicode = data["fechaInicio"]
            proyecto.fechaInicio = None
            if fechaInicioUnicode is not None:
                proyecto.fechaInicio = datetime.strptime(fechaInicioUnicode, '%Y-%m-%d')
            algoCambio = True
        if data.has_key("fechaFinal"):
            fechaFinalUnicode = data["fechaFinal"]
            proyecto.fechaFinal = None
            if fechaFinalUnicode is not None:
                proyecto.fechaFinal = datetime.strptime(fechaFinalUnicode, '%Y-%m-%d')
            algoCambio = True
        if data.has_key("prioridad"):
            proyecto.prioridad = data["prioridad"]
            algoCambio = True
        if data.has_key("avance"):
            proyecto.avance = data["avance"]
            algoCambio = True
        if data.has_key("estado"):
            proyecto.estado = data["estado"]
            algoCambio = True
        if data.has_key("idPatrocinador"):
            idPatrocinador = data["idPatrocinador"]
            algoCambio = True
            patrocinador = Patrocinador.objects.get(id=idPatrocinador)
            if patrocinador is None:
                raise ValidationError({'idPatrocinador': ['No existe este patrocinador']})
            proyecto.patrocinador = patrocinador
        if algoCambio:
            proyecto.save()
        return HttpResponse(serializers.serialize("json", [proyecto]))
    # Si es GET Lista
    elif request.method == 'GET':
        proyecto = Proyecto.objects.get(id=id)
        return HttpResponse(serializers.serialize("json", [proyecto]))
    else:
        raise NotFound(detail="No se encuentra comando rest proyectos con metodo " + request.method)