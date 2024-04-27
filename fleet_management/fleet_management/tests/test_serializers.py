"""Módulo que contiene pruebas para los serializadores de la aplicación."""
from datetime import datetime
from django.test import TestCase
from ..models import Taxi
from ..serializers import TaxiSerializer, LocationHistorySerializer

# pylint: disable=no-member
class TaxiSerializerTest(TestCase):
    """Pruebas para el serializador TaxiSerializer."""
    def test_taxi_serializer(self):
        """Prueba la funcionalidad del serializador TaxiSerializer."""
        taxi = Taxi.objects.create(plate='DEF987')
        serializer = TaxiSerializer(taxi)
        self.assertEqual(serializer.data['plate'], 'DEF987')

class LocationHistorySerializerTestCase(TestCase):
    """Caso de prueba para el LocationHistorySerializer."""
    def setUp(self):
        self.taxi = Taxi.objects.create(plate="ABC123")
        self.location_history_data = {
            "taxi_id": self.taxi.id,
            "date": datetime.now(),
            "latitude": 20.7125,
            "longitude": -54.0065
        }
        self.serializer = LocationHistorySerializer(data=self.location_history_data)

    def test_serializer_with_valid_data(self):
        """Prueba la serialización con datos válidos."""
        self.assertTrue(self.serializer.is_valid())

    def test_serializer_with_invalid_data(self):
        """Prueba la serialización con datos inválidos."""
        invalid_location_history_data = {
            "taxi_id": 99,
            "date": "invalid_date_format",
            "latitude": "invalid_latitude",
            "longitude": "invalid_longitude"
        }
        serializer_with_invalid_data = LocationHistorySerializer(data=invalid_location_history_data)
        self.assertFalse(serializer_with_invalid_data.is_valid())
