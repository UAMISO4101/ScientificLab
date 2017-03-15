from django.test import TestCase
from .models import Patrocinador
from .models import Proyecto
from django.utils import timezone


# Create your tests here.

class PatrocinadorMethodTests(TestCase):

    def create_Patrocinador (self, nombre="Bayer"):
        return Patrocinador.objects.create(nombre=nombre)

    def test_creation(self):
        p = self.create_Patrocinador("Bayer")
        self.assertTrue(isinstance(p, Patrocinador))

    def test_update (self):
         p = self.create_Patrocinador("Bayer")
         Patrocinador.objects.filter(nombre="Bayer").update(nombre='Bayyer')
         patrocinador = Patrocinador.objects.get(nombre="Bayyer")
         self.assertEqual(patrocinador.nombre, "Bayyer")

    def test_delete (self):
        p = self.create_Patrocinador("Bayer")
        Patrocinador.objects.filter(nombre="Bayer").delete()
        try:
            patrocinador = Patrocinador.objects.get(nombre="Bayer")
        except Patrocinador.DoesNotExist:
            patrocinador = None
        self.assertEqual(patrocinador, None)

class ProyectoMethodTests(TestCase):
    def create_Patrocinador (self, nombre="Bayer"):
        return Patrocinador.objects.create(nombre=nombre)

    def test_creation(self):
        patrocinador = self.create_Patrocinador("Bayer")
        p= Proyecto.objects.create(
        nombre="Protecto1",
        descripcion = "Proyecto test",
        fechaInicio = timezone.now(),
        fechaFinal =  timezone.now(),
        prioridad = 1,
        avance = 90,
        estado =1,
        patrocinador = patrocinador)
        self.assertTrue(isinstance(p, Proyecto))

    def test_update(self):
        patrocinador = self.create_Patrocinador("Bayer")
        p = Proyecto.objects.create(
            nombre="Protecto1",
            descripcion="Proyecto test",
            fechaInicio=timezone.now(),
            fechaFinal=timezone.now(),
            prioridad=1,
            avance=90,
            estado=1,
            patrocinador=patrocinador)
        proyecto = Proyecto.objects.get(nombre="Protecto1")
        self.assertEqual(proyecto.nombre, "Protecto1")

    def test_delete (self):
        patrocinador = self.create_Patrocinador("Bayer")
        p = Proyecto.objects.create(
            nombre="Proyecto1",
            descripcion="Proyecto test",
            fechaInicio=timezone.now(),
            fechaFinal=timezone.now(),
            prioridad=1,
            avance=90,
            estado=1,
            patrocinador=patrocinador)
        Proyecto.objects.filter(nombre="Proyecto1").delete()
        try:
            proyectos = Proyecto.objects.get(nombre="Proyecto1")
        except Proyecto.DoesNotExist:
            proyectos = None
        self.assertEqual(proyectos, None)