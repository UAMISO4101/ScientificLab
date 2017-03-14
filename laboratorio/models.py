from __future__ import unicode_literals
from django.db import models


# Clase Patrocinador: Define un Patrocinador de proyectos
class Patrocinador(models.Model):
    nombre = models.CharField(max_length=250, null=True)

# Clase Proyecto: Define un Proyecto del Laboratorio auspiciado por una persona
class Proyecto(models.Model):
    INICIADO = 0;
    TERMINADO = 1;
    EN_PROGRESO = 2;
    CANCELADO = 3;
    PAUSADO = 4;
    ESTADO_CHOICES = (
        (INICIADO, 'Iniciado'),
        (TERMINADO, 'Terminado'),
        (EN_PROGRESO, 'En Progreso'),
        (CANCELADO, 'Cancelado'),
        (PAUSADO, 'Pausado'),
    )
    nombre = models.CharField(max_length=250, null=True)
    descripcion = models.CharField(max_length=1000, null=True)
    fechaInicio = models.DateField(null=True)
    fechaFinal = models.DateField(null=True)
    prioridad = models.IntegerField(null=True)
    avance = models.FloatField(null=True)
    estado = models.IntegerField(choices=ESTADO_CHOICES,null=True)
    patrocinador = models.ForeignKey(Patrocinador, related_name='proyectos', null=True, on_delete=models.CASCADE)

# Clase Responsable: Define un responsable de proyecto
class Responsable(models.Model):
    nombre = models.CharField(max_length=250, null=True)

# Clase Experimento: Define un experimento dentro de un proyecto
class Experimento(models.Model):
    INICIADO = 0;
    TERMINADO = 1;
    EN_PROGRESO = 2;
    CANCELADO = 3;
    PAUSADO = 4;
    ESTADO_CHOICES = (
        (INICIADO, 'Iniciado'),
        (TERMINADO, 'Terminado'),
        (EN_PROGRESO, 'En Progreso'),
        (CANCELADO, 'Cancelado'),
        (PAUSADO, 'Pausado'),
    )
    EXITOSO = 0;
    FALLIDO = 1;
    RESULTADO_CHOICES = (
        (EXITOSO, 'Exitoso'),
        (FALLIDO, 'Fallido'),
    )
    nombre = models.CharField(max_length=250, null=True)
    descripcion = models.CharField(max_length=1000, null=True)
    fechaInicio = models.DateField(null=True)
    prioridad = models.IntegerField(null=True)
    estado = models.IntegerField(choices=ESTADO_CHOICES,null=True)
    resultado = models.IntegerField(choices=RESULTADO_CHOICES,null=True)
    proyecto = models.ForeignKey(Proyecto, related_name='experimentos', null=True, on_delete=models.CASCADE)
    responsable = models.ForeignKey(Responsable, related_name='experimentos', null=True, on_delete=models.CASCADE)

# Clase Protocolo: Define los protocolos que pueden ir en un experimento
class Protocolo(models.Model):
    HONGOS = 0;
    BACTERIAS = 1;
    ADN_EXTRACCION = 2;
    PRUEBAS_BIOLOGICAS = 3;
    CATEGORIA_CHOICES = (
        (HONGOS, 'Hongos'),
        (BACTERIAS, 'Bacterias'),
        (ADN_EXTRACCION, 'Extraccion ADN'),
        (PRUEBAS_BIOLOGICAS, 'Pruebas Biologicas'),
    )
    titulo = models.CharField(max_length=250, null=True)
    descripcion = models.CharField(max_length=1000, null=True)
    version = models.IntegerField(null=True)
    categoria = models.IntegerField(choices=CATEGORIA_CHOICES,null=True)
    experimentos = models.ManyToManyField(Experimento, through='ProtocolosExperimento')

# Clase ProtocolosExperimento: Define los protocolos de un experimento
class ProtocolosExperimento(models.Model):
    protocolo = models.ForeignKey(Protocolo)
    experimento = models.ForeignKey(Experimento)

# Clase Paso: Define un paso de un protocolo
class Paso(models.Model):
    nombre = models.CharField(max_length=250, null=True)
    protocolos = models.ForeignKey(Protocolo, related_name='pasos', null=True, on_delete=models.CASCADE)

# Clase Elemento: Define un elemento del laboratorio
class Elemento(models.Model):
    CMS = 0;
    GRAMOS = 1;
    CM_CUBICO = 2;
    UNIDADES = 3;
    UNIDADES_CHOICES = (
        (CMS, 'Centimetros'),
        (GRAMOS, 'Gramos'),
        (CM_CUBICO, 'Centimetros cubicos'),
        (UNIDADES, 'Unidades'),
    )
    nombre = models.CharField(max_length=250, null=True)
    cantidad = models.FloatField(null=True)
    unidades = models.IntegerField(choices=UNIDADES_CHOICES, null=True)
    pasos = models.ForeignKey(Paso, related_name='elementos', null=True, on_delete=models.CASCADE)

