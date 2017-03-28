from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import Protocolo

class ProtocoloSerializer(serializers.ModelSerializer):
    class Meta:
        model = Protocolo
        fields = ('titulo','descripcion', 'version', 'categoria')