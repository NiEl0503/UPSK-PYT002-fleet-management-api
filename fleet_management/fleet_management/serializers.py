"""Módulo que convierte los objetos en formato JSON."""

from rest_framework import serializers
from .models import Taxi

class TaxiSerializer(serializers.ModelSerializer):
    """Serializador para el modelo Taxi."""
    class Meta:
        """Proporciona metainformación adicional."""
        model = Taxi
        fields = ['id', 'plate']
