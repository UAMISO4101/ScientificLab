import json
import time
from django.http import JsonResponse
from django.core import serializers
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.exceptions import ValidationError, NotFound
from datetime import datetime
from ..models import Experimento, Proyecto, Responsable, Protocolo, ResultadoExperimento, EstadoProyecto, \
    ProtocolosExperimento
from django.shortcuts import render
from rest_framework import generics
from ..serializers import ExperimentoSerializer, ProtocolosXExperimentoProyectoSerealizer


class ExperimentoLista(generics.ListAPIView):
    serializer_class = ExperimentoSerializer
    def get_queryset(self):
        proyecto = self.request.query_params.get('proyecto')
        if(proyecto !=0 ):
            experimentos = Experimento.objects.filter(proyecto = proyecto).order_by('responsable')
        else:
            experimentos = Experimento.objects.all()
        return experimentos

class ProtocolosExperimentosProyecto(generics.ListAPIView):
    serializer_class = ProtocolosXExperimentoProyectoSerealizer
    #Trazabilidad: Protocolos finalizados
    def get_queryset(self):
        id = self.request.query_params.get('id')
        print(id)
        listExperimentos = list()
        if (id):
            for Resp in Experimento.objects.filter(proyecto_id=id).select_related('proyecto'):
                for Proto in ProtocolosExperimento.objects.filter(experimento_id=Resp.id):
                    listExperimentos.append(Resp)
        return listExperimentos

class ExperimentosProyecto(generics.ListAPIView):
    serializer_class = ProtocolosXExperimentoProyectoSerealizer
    #Trazabilidad: Protocolos finalizados
    def get_queryset(self):
        id = self.request.query_params.get('id')
        print(id)
        listExperimentos = list()
        if (id):
            for Resp in Experimento.objects.filter(proyecto_id=id).select_related('proyecto'):
                listExperimentos.append(Resp)
        return listExperimentos

def agregar_experimento(request, idProy):
    proyecto = Proyecto.objects.get(id=idProy)
    return render(request, 'laboratorio/Experimento/agregarExperimento.html', {"idProy": idProy, "nombreProyecto": proyecto.nombre})


def listar_experimentos(request, idProy):
    proyecto = Proyecto.objects.get(id=idProy)
    return render(request, 'laboratorio/Experimento/experimentos.html', {"idProy": idProy, "nombreProyecto": proyecto.nombre})

def agregar_expeprotocolo(request, idExp):
    return render(request, 'laboratorio/Experimento/agregarExperimentoProtocolo.html',
                  {"experimento": Experimento.objects.get(id=idExp)})


def detallar_experimento(request, idExp):
    return render(request, 'laboratorio/Experimento/detallarExperimento.html', {"experimento": Experimento.objects.get(id=idExp)})


def editar_experimento(request, idExp):
    experimento= Experimento.objects.get(id=idExp)
    proy = Proyecto.objects.get(id=experimento.proyecto.id)
    return render(request, 'laboratorio/Experimento/editarExperimento.html',
                  {"experimento": Experimento.objects.get(id=idExp),"nombreProyecto": proy.nombre})


#Atiende las peticiones de los Experimentos
@csrf_exempt
def experimentos(request):

    if request.method == 'POST':
        data = request.POST
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
            if fechaInicioUnicode is not None and fechaInicioUnicode is not u'':
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

    elif request.method == 'GET':
        experimentos = Experimento.objects.all()
        return HttpResponse(serializers.serialize("json", experimentos), content_type="application/json")
    else:
        raise NotFound(detail="No se encuentra comando rest experimentos con metodo " + request.method)



@csrf_exempt
def experimentos_id(request, id):
    if request.method == 'DELETE':
        try:
            experimento = Experimento.objects.get(id=id)
        except:
            raise ValidationError({'id': ['No existe experimento ' + id]})
        experimento.delete()
        return JsonResponse({"Mensaje":"Experimento " + id + " borrado"})

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
            if fechaInicioUnicode is not None and fechaInicioUnicode is not u'':
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

    elif request.method == 'GET':
        try:
            experimento = Experimento.objects.get(id=id)
        except:
            raise ValidationError({'id': ['No existe experimento ' + id]})
        return HttpResponse(serializers.serialize("json", [experimento]), content_type="application/json")
    else:
        raise NotFound(detail="No se encuentra comando rest experimentos/{id} con metodo " + request.method)

@csrf_exempt
def proyecto_id_experimentos(request, id):

    if request.method == 'GET':
        return render(request, 'laboratorio/Experimento/experimentos.html', {"proy": Proyecto.objects.get(proyecto=id)})


#Atiende las peticiones de un Experimento determinado
@csrf_exempt
def experimentos_id_protocolos(request, id):

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

    if request.method == 'GET':
        try:
            resultados = ResultadoExperimento().getDict()
        except:
            raise ValidationError({'id': ['No fue posible generar la lista de resultados de experimento']})
        return HttpResponse(json.dumps(resultados), content_type="application/json")
    else:
        raise NotFound(detail="No se encuentra comando rest resultadosexperimento/ con metodo " + request.method)


#Atiende las peticiones de Estados del Experimento
@csrf_exempt
def lista_estados_experimento(request):

    if request.method == 'GET':
        try:
            estados = ResultadoExperimento().getDictStates()
        except:
            raise ValidationError({'id': ['No fue posible generar la lista de estados del experimento']})
        return HttpResponse(json.dumps(estados), content_type="application/json")
    else:
        raise NotFound(detail="No se encuentra comando rest estadosexperimento/ con metodo " + request.method)


@csrf_exempt
def lista_nombre_proyecto(request):

    if request.method == 'GET':
        try:
            Nombre_proyectos = Proyecto.objects.all()
        except:
            raise ValidationError({'id': ['No existen proyecto']})
        return HttpResponse(serializers.serialize("json", Nombre_proyectos), content_type="application/json")

    else:
        raise NotFound(detail="No se encuentra comando rest nombreProyecto/ con metodo " + request.method)

@csrf_exempt
def start_experiment(request, id):
    if request.method == 'POST':
        try:
            experimento = Experimento.objects.get(id=id)
            if experimento.fechaInicio is None:
                experimento.fechaInicio = datetime.now()
                experimento.estado = 0
        except:
            raise ValidationError({'id': ['No existe experimento ' + id]})
        experimento.save()
        return HttpResponse(serializers.serialize("json", [experimento]), content_type="application/json")
    else:
        raise NotFound(detail="No se encuentra comando rest experimentos/{id} con metodo " + request.method)