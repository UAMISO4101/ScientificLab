from django.contrib.auth.models import User, Group
from rest_framework import serializers

from laboratorio.models import Avance
from .models import Protocolo, Proyecto, Experimento, Responsable

class ProtocoloSerializer(serializers.ModelSerializer):
    class Meta:
        model = Protocolo
        fields = ('id','titulo','descripcion', 'version', 'categoria')


class ProyectoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Proyecto
        fields = ('pk', 'nombre', 'avance', 'estado', 'prioridad', 'fechaInicio')


class ExperimentoSerializer(serializers.ModelSerializer):
    responsable = serializers.StringRelatedField(many=False)
    estado =  serializers.SerializerMethodField()
    resultado = serializers.SerializerMethodField()
    class Meta:
        model = Experimento
        fields = ('id', 'nombre', 'estado', 'prioridad', 'fechaInicio', 'proyecto', 'responsable', 'resultado')

    def get_estado(self, obj):
        return obj.get_estado_display()

    def get_resultado(self, obj):
        return obj.get_resultado_display()

# Clase serializadora de clase usuario
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'password', 'first_name', 'last_name', 'email')

# Clase serializadora de clase de avance del proyecto
class AvanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Avance
        fields = ('id', 'fecha', 'reporte', 'comentario')

class ResponsableSerializer(serializers.ModelSerializer):
    class Meta:
        model = Responsable
        fields = ('id', 'nombre', 'username', 'email', 'celular', 'cargo')
