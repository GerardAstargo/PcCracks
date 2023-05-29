from django.contrib import admin
from django.urls import path, include
from .views import *


urlpatterns = [
    path('', menu_off, name='menu_off'),
    path('menuON/', menu_on, name='menu_on'),
    path('mapaOFF/', mapa_off, name='mapa_off'),
    path('mapaON/', mapa_on, name='mapa_on'),
    path('login/', login, name='login'),
    path('Forgot_password/', forgot_password, name='forgot_password'),
    path('menuOFFproductos/', menu_off_productos, name='menu_off_productos'),
    path('menuONproductos/', menu_on_productos, name='menu_on_productos'),
    path('admin/', admin_agregar, name='admin_agregar'),
    path('admined/', admin_editar, name='admin_editar'),
    path('adminel/', admin_eliminar, name='admin_eliminar'),
    path('cuenta/', cuenta, name='cuenta'),
    path('modificarCuenta/', modificarCuenta, name='modificarCuenta'),
    path('carrito/', carrito, name='carrito'),
    path('registro/', registro, name='registro'),
    path('agregarCliente/',agregarCliente,name="agregarCliente"),


    
    
    path('menuFastONRam/', menu_fast_on_ram, name='menu_fast_on_ram'),
    path('menuFastONProcesador/', menu_fast_on_procesador, name='menu_fast_on_procesador'),
    path('menuFastONPlaca/', menu_fast_on_placa, name='menu_fast_on_placa'),
    path('menuFastONPerifericos/', menu_fast_on_perifericos, name='menu_fast_on_perifericos'),
    path('menuFastONGpu/', menu_fast_on_gpu, name='menu_fast_on_gpu'),
    path('menuFastONGabinete/', menu_fast_on_gabinete, name='menu_fast_on_gabinete'),
    path('menuFastONFuente/', menu_fast_on_fuente, name='menu_fast_on_fuente'),
    path('menuFastONAlmacenamiento/', menu_fast_on_almacenamiento, name='menu_fast_on_almacenamiento'),

    path('menuFastOFFRam/', menu_fast_off_ram, name='menu_fast_off_ram'),
    path('menuFastOFFProcesador/', menu_fast_off_procesador, name='menu_fast_off_procesador'),
    path('menuFastOFFPlaca/', menu_fast_off_placa, name='menu_fast_off_placa'),
    path('menuFastOFFPerifericos/', menu_fast_off_perifericos, name='menu_fast_off_perifericos'),
    path('menuFastOFFGpu/', menu_fast_off_gpu, name='menu_fast_off_gpu'),
    path('menuFastOFFGabinete/', menu_fast_off_gabinete, name='menu_fast_off_gabinete'),
    path('menuFastOFFFuente/', menu_fast_off_fuente, name='menu_fast_off_fuente'),
    path('menuFastOFFAlmacenamiento/', menu_fast_off_almacenamiento, name='menu_fast_off_almacenamiento'),



]
