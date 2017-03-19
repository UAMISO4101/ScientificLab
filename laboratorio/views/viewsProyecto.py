import json
from django.http import JsonResponse
from django.core import serializers
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.exceptions import ValidationError, NotFound
from datetime import datetime
from ..models import Proyecto, Patrocinador, Experimento
from django.shortcuts import render


def agregar_proyecto(request):
    return render(request, 'laboratorio/agregarProyecto.html')


#Atiende las peticiones de los Proyectos
def proyectos(request):
    # Si es GET Lista
    if request.method == 'GET':
        return render(request, 'laboratorio/proyectos.html', {"proyectos": Proyecto.objects.all()})
    else:
        raise NotFound(detail="No se encuentra comando rest proyectos con metodo " + request.method)


@csrf_exempt
def crear_proyecto(request):
    if request.method == 'POST':
        data = request.POST
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
        estado =  0
        idPatrocinador = (int)(data["patrocinador"])
        try:
            patrocinador = Patrocinador.objects.get(id=idPatrocinador)
        except:
            raise ValidationError({'idPatrocinador': ['No existe patrocinador ' + idPatrocinador]})

        proyecto = Proyecto(nombre=nombre, descripcion=descripcion, fechaInicio=fechaInicio, fechaFinal=fechaFinal, prioridad=prioridad, avance=avance, patrocinador=patrocinador, estado=estado)
        proyecto.save()
        return render(request, 'laboratorio/proyectos.html', {"proyectos": Proyecto.objects.all()})

    else:
        return render(request, 'laboratorio/agregarProyecto.html')


#Atiende las peticiones de un Proyecto determinado
@csrf_exempt
def proyectos_id(request, id):

    # Si es DELETE Borra
    if request.method == 'DELETE':
        try:
            proyecto = Proyecto.objects.get(id=id)
        except:
            raise ValidationError({'id': ['No existe Proyecto ' + id]})
        proyecto.delete()
        return JsonResponse({"Mensaje":"Proyecto " + id + " borrado"})
    # Si es PUT Actualiza
    elif request.method == 'PUT':
        try:
            proyecto = Proyecto.objects.get(id=id)
        except:
            raise ValidationError({'id': ['No existe Proyecto ' + id]})
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
            try:
                patrocinador = Patrocinador.objects.get(id=idPatrocinador)
            except:
                raise ValidationError({'idPatrocinador': ['No existe patrocinador ' + idPatrocinador]})
            proyecto.patrocinador = patrocinador
        if algoCambio:
            proyecto.save()
        return HttpResponse(serializers.serialize("json", [proyecto]), content_type="application/json")
    # Si es GET Lista
    elif request.method == 'GET':
        try:
            proyecto = Proyecto.objects.get(id=id)
        except:
            raise ValidationError({'id': ['No existe Proyecto ' + id]})
        return HttpResponse(serializers.serialize("json", [proyecto]), content_type="application/json")
    else:
        raise NotFound(detail="No se encuentra comando rest proyectos/{id} con metodo " + request.method)


#Atiende las peticiones de un Proyecto determinado
@csrf_exempt
def proyectos_id_experimentos(request, id):
    # Si es GET Lista
    if request.method == 'GET':
        try:
            proyecto = Proyecto.objects.get(id=id)
        except:
            raise ValidationError({'id': ['No existe proyecto ' + id]})
        experimentos = Experimento.objects.filter(proyecto=proyecto)
        return HttpResponse(serializers.serialize("json", experimentos), content_type="application/json")
    else:
        raise NotFound(detail="No se encuentra comando rest proyectos/{id}/experimentos con metodo " + request.method)

