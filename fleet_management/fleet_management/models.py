"""Módulo que contiene la definición de los modelos de la aplicación."""

from django.db import models

class Taxi(models.Model):
    """Modelo que representa un taxi en el sistema."""
    plate = models.CharField(max_length=20)

    class Meta:
        """taxis nombre de la tabla en la bdd"""
        db_table = 'taxis'

class LocationHistory(models.Model):
    """Modelo que representa el historial de localizaciones de un taxi."""
    id = models.AutoField(primary_key=True)
    taxi = models.ForeignKey(Taxi, on_delete=models.CASCADE)
    date = models.DateTimeField()
    latitude = models.FloatField()
    longitude = models.FloatField()

    class Meta:
        """trajectories nombre de la tabla en la bdd"""
        db_table = 'trajectories'
