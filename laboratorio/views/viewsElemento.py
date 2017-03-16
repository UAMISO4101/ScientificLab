import json
from django.http import JsonResponse
from django.core import serializers
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.exceptions import ValidationError, NotFound
from ..models import Elemento, Paso

#Atiende las peticiones de los Elementos
@csrf_exempt
def elementos(request):

    # Si es POST Graba
    if request.method == 'POST':
        data = json.loads(request.body)
        nombre = data["nombre"]
        cantidad = data["cantidad"]
        unidades = data["unidades"]
        idPaso = data["idPaso"]
        paso = Paso.objects.get(id=idPaso)
        if paso is None:
            raise ValidationError({'idPaso': ['No existe paso ' + idPaso]})
        elemento = Elemento(nombre=nombre, cantidad=cantidad, unidades=unidades, paso=paso)
        elemento.save()
        return HttpResponse(serializers.serialize("json", [elemento]))
    # Si es GET Lista
    elif request.method == 'GET':
        elementos = Elemento.objects.all()
        return HttpResponse(serializers.serialize("json", elementos))
    else:
        raise NotFound(detail="No se encuentra comando rest elementos con metodo " + request.method)

#Atiende las peticiones de un Elemento determinado
@csrf_exempt
def elementos_id(request, id):

    # Si es DELETE Borra
    if request.method == 'DELETE':
        elemento = Elemento.objects.get(id=id)
        elemento.delete()
        return JsonResponse({"Mensaje":"Elemento " + id + " borrado"})
    # Si es PUT Actualiza
    elif request.method == 'PUT':
        elemento = Elemento.objects.get(id=id)
        data = json.loads(request.body)
        algoCambio = False
        if data.has_key("nombre"):
            elemento.nombre = data["nombre"]
            algoCambio = True
        if data.has_key("cantidad"):
            elemento.cantidad = data["cantidad"]
            algoCambio = True
        if data.has_key("unidades"):
            elemento.unidades = data["unidades"]
            algoCambio = True
        if data.has_key("idPaso"):
            idPaso = data["idPaso"]
            algoCambio = True
            paso = Paso.objects.get(id=idPaso)
            if paso is None:
                raise ValidationError({'idPaso': ['No existe paso ' + idPaso]})
            elemento.paso = paso
        if algoCambio:
            elemento.save()
        return HttpResponse(serializers.serialize("json", [elemento]))
    # Si es GET Lista
    elif request.method == 'GET':
        elemento = Elemento.objects.get(id=id)
        return HttpResponse(serializers.serialize("json", [elemento]))
    else:
        raise NotFound(detail="No se encuentra comando rest elementos con metodo " + request.method)