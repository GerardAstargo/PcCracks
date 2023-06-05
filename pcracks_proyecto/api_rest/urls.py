from django.urls import path
from api_rest.views import lista_clientes

urlpatterns = [
    path('lista_clientes/', lista_clientes, name='lista_clientes')
]