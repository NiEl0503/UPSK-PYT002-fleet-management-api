"""Módulo que contiene pruebas para las vistas de la aplicación."""
from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from ..models import Taxi

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
