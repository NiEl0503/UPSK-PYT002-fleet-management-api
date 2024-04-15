"""Módulo que contiene pruebas para los serializadores de la aplicación."""
from django.test import TestCase
from ..models import Taxi
from ..serializers import TaxiSerializer

# pylint: disable=no-member
class TaxiSerializerTest(TestCase):
    """Pruebas para el serializador TaxiSerializer."""
    def test_taxi_serializer(self):
        """Prueba la funcionalidad del serializador TaxiSerializer."""
        taxi = Taxi.objects.create(plate='DEF987')
        serializer = TaxiSerializer(taxi)
        self.assertEqual(serializer.data['plate'], 'DEF987')
