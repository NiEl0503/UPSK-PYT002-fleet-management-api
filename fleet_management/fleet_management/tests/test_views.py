"""Módulo que contiene pruebas para las vistas de la aplicación."""
from datetime import datetime
from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient, APIRequestFactory
from rest_framework import status
from ..models import Taxi, LocationHistory
from ..views import LocationHistoryList

# pylint: disable=no-member
class TaxiListTest(TestCase):
    """Pruebas para la vista TaxiList."""
    def setUp(self):
        """Configuración inicial para las pruebas."""
        self.client = APIClient()
        self.taxi1 = Taxi.objects.create(plate='ABC123')
        self.taxi2 = Taxi.objects.create(plate='XYZ456')

    def test_list_taxis(self):
        """Prueba para listar taxis."""
        url = reverse('taxi-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 2)

    def test_pagination(self):
        """Prueba para la paginación de la vista."""
        for _ in range(12):
            Taxi.objects.create(plate='TEST')
        url = reverse('taxi-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 10)

class LocationHistoryListViewTestCase(TestCase):
    """Caso de prueba para la vista LocationHistoryList."""
    def setUp(self):
        self.factory = APIRequestFactory()
        self.taxi = Taxi.objects.create(plate="ABC123")
        self.location_history = LocationHistory.objects.create(
            taxi=self.taxi,
            date=datetime.now(),
            latitude=90.7168,
            longitude=-14.0360
        )

    def test_location_history_list_view(self):
        """Realizando solicitud GET simulada a la vista LocationHistoryList con un
        taxi_id y una fecha específica"""
        request = self.factory.get('/location_history/', {'taxi_id': self.taxi.id, 'date': '2008-02-02'})
        view = LocationHistoryList.as_view()
        response = view(request)
        self.assertEqual(response.status_code, 200)
        