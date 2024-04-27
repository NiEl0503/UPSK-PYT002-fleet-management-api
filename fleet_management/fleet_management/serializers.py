"""Módulo que convierte los objetos en formato JSON."""

from rest_framework import serializers
from .models import LocationHistory, Taxi

class TaxiSerializer(serializers.ModelSerializer):
    """Serializador para el modelo Taxi."""
    class Meta:
        """Proporciona metainformación adicional."""
        model = Taxi
        fields = ['id', 'plate']

class LocationHistorySerializer(serializers.ModelSerializer):
    """Serializador para el modelo LocationHistory."""
    class Meta:
        """Proporciona metainformación adicional."""
        model = LocationHistory
        fields = ['id', 'taxi_id', 'date', 'latitude', 'longitude']

class LastLocationSerializer(serializers.ModelSerializer):
    """Serializador para la última localización de un taxi."""
    plate = serializers.CharField(source='taxi.plate', read_only=True)
    timestamp = serializers.DateTimeField(source='date', read_only=True)
    class Meta:
        """Proporciona metainformación adicional."""
        model = LocationHistory
        fields = ['taxi', 'plate', 'latitude', 'longitude', 'timestamp']
