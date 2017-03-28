from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import Protocolo, Proyecto

class ProtocoloSerializer(serializers.ModelSerializer):
    class Meta:
        model = Protocolo
        fields = ('titulo', 'descripcion', 'version', 'categoria')


class ProyectoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Proyecto
        fields = ('pk', 'nombre', 'avance', 'estado', 'prioridad', 'fechaInicio')