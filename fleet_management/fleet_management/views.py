"""Módulo que contiene la definición de las vistas de la aplicación."""
from rest_framework import generics, pagination
from .models import LocationHistory, Taxi
from .serializers import LocationHistorySerializer, TaxiSerializer, LastLocationSerializer

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

class LocationHistoryList(generics.ListAPIView):
    """Vista para obtener el historial de localizaciones de un taxi en una fecha dada."""
    serializer_class = LocationHistorySerializer
    pagination_class = CustomPagination

    def get_queryset(self):
        taxi_id = self.request.query_params.get('taxi_id')
        date = self.request.query_params.get('date')
        if taxi_id is not None and date is not None:
            return LocationHistory.objects.filter(taxi_id=taxi_id, date__date=date)
        return LocationHistory.objects.none()

class LastLocationList(generics.ListAPIView):
    """Vista para obtener la última localización reportada por cada taxi."""
    serializer_class = LastLocationSerializer
    pagination_class = CustomPagination

    def get_queryset(self):
        queryset = LocationHistory.objects.order_by('taxi', '-date').distinct('taxi')
        return queryset
    