from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import Protocolo, Proyecto, Experimento

class ProtocoloSerializer(serializers.ModelSerializer):
    class Meta:
        model = Protocolo
        fields = ('id','titulo','descripcion', 'version', 'categoria')


class ProyectoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Proyecto
        fields = ('pk', 'nombre', 'avance', 'estado', 'prioridad', 'fechaInicio')


class ExperimentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Experimento
        fields = ('id', 'nombre', 'estado', 'prioridad', 'fechaInicio', 'proyecto', 'responsable', 'resultado')