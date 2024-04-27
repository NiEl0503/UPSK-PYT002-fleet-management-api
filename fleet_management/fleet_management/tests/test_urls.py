"""Módulo que contiene pruebas para las URL de la aplicación."""

from django.test import SimpleTestCase
from django.urls import reverse, resolve
from ..views import TaxiList

class TestUrls(SimpleTestCase):
    """Pruebas para las URL de la aplicación."""
    def test_taxi_list_url_resolves(self):
        """Prueba que la URL de listar taxis se resuelve correctamente."""
        url = reverse('taxi-list')
        self.assertEqual(resolve(url).func.view_class, TaxiList)
        