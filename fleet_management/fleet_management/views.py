"""Módulo que contiene la definición de las vistas de la aplicación."""
from rest_framework import generics, pagination
from .models import Taxi
from .serializers import TaxiSerializer

class CustomPagination(pagination.PageNumberPagination):
    """Especifica cómo se deben paginar los resultados de esta vista"""
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 300

# pylint: disable=no-member
class TaxiList(generics.ListAPIView):
    """Vista para listar todos los taxis."""
    serializer_class = TaxiSerializer
    pagination_class = CustomPagination

    def get_queryset(self):
        return Taxi.objects.all()
