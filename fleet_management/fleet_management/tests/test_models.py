"""Módulo que contiene las pruebas para los modelos de la aplicación."""
from django.test import TestCase
from ..models import Taxi

# pylint: disable=no-member
class TaxiModelTest(TestCase):
    """prueba para el modelo Taxi"""
    def setUp(self):
        """taxi creado para usar en la prueba"""
        Taxi.objects.create(plate='DEF987')

    def test_taxi_creation(self):
        """Obtener el taxi creado en el método setUp"""
        taxi = Taxi.objects.get(plate='DEF987')
        self.assertEqual(taxi.plate, 'DEF987')
