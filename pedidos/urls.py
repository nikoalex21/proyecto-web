from django.urls import path
from . import views


urlpatterns = [
    path('', views.procesar_pedido, name="procesar_pedido"),
    path('pagar/', views.pasarela_pago, name="pasarela_pago"),

]