"""Módulo que define los patrones de URL para una aplicación web."""
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.contrib import admin
from django.urls import path
from .views import LocationHistoryList, TaxiList

SchemaView = get_schema_view(
   openapi.Info(
      title="Fleet Management",
      default_version='v1',
      description="Test description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="ncontreraskanan@gmail.com"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
)

urlpatterns = [
   path('admin/', admin.site.urls),
   path('taxis/', TaxiList.as_view(), name='taxi-list'),
   path('location_history/', LocationHistoryList.as_view(), name='location-history'),
   path('docs/', SchemaView.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]
