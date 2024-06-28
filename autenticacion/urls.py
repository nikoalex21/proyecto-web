from django.urls import path
from .views import VRegistro, cerrar_sesion, inicio_sesion


urlpatterns = [
    path('',VRegistro.as_view(), name="autenticacion"),
    path('cerrar_sesion',cerrar_sesion, name="cerrar_sesion"),
    path('inicio_sesion',inicio_sesion, name="inicio_sesion"),

   
]
