from django.urls import path
from api_rest.views import lista_clientes,detalle_cliente

urlpatterns = [
    path('lista_clientes/', lista_clientes, name='lista_clientes'),
    path('detalle_cliente/<id>', detalle_cliente, name='detalle_cliente'),
]