"""pcracks_proyecto URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from pcracks import views 
from pcracks.views import agregar_producto_carrito,eliminar_producto_carrito,restar_producto_carrito,limpiar_carrito


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('pcracks.urls')),
    path('buscar/',views.buscar),
    path('api/', include('api_rest.urls')),
    path('agregar/<id>', agregar_producto_carrito, name="Add"),
    path('eliminar/<id>', eliminar_producto_carrito, name="Del"),
    path('restar/<id>', restar_producto_carrito, name="Sub"),
    path('limpiar/', limpiar_carrito, name="CLS"),


    
]

if settings.DEBUG:
    urlpatterns += static (settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
