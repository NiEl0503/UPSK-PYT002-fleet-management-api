"""Módulo que contiene las pruebas para los modelos de la aplicación."""
from django.test import TestCase
from django.utils import timezone
from ..models import Taxi
from ..serializers import LocationHistory

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

class LocationHistoryModelTest(TestCase):
    """Prueba para el modelo LocationHistory."""
    def test_location_history_model(self):
        """Prueba la creación de un historial de localización."""
        taxi = Taxi.objects.create(plate="DEF456")
        date = timezone.now()
        location_history = LocationHistory.objects.create(taxi=taxi, date=date, latitude=40.7128, longitude=-74.0060)
        self.assertEqual(location_history.taxi_id, taxi.id)
        self.assertEqual(location_history.date, date)
        self.assertEqual(location_history.latitude, 40.7128)
        self.assertEqual(location_history.longitude, -74.0060)
