from django.shortcuts import render
from django.http import HttpResponse
from pcracks.models import Producto

# Create your views here.
def menu_off (request):
    return render(request, 'pcracks/menuOFF.html')
def buscar(request):
    if request.GET["barra_buscar"]:
        #mensaje="Articulo buscado: %r" %request.GET["barra_buscar"]
        prd=request.GET["barra_buscar"]
        articulos=Producto.objects.filter(marca__icontains=prd)
        return render(request, "pcracks/resultados_busqueda.html", {"articulos": articulos, "query":prd})

    else:
        mensaje="no has introducido nada"
    return HttpResponse(mensaje)

def menu_on (request):
    return render (request, 'pcracks/menuON.html')

def mapa_off (request):
    return render (request, 'pcracks/mapaOFF.html')

def mapa_on (request):
    return render (request, 'pcracks/mapaON.html')

def login (request):
    return render (request, 'pcracks/Login.html')

def forgot_password (request):
    return render (request, 'pcracks/Forgot_password.html')

def menu_off_productos (request):
    return render (request, 'pcracks/menuOFFproductos.html')

def menu_on_productos (request):
    return render (request, 'pcracks/menuONproductos.html')

def admin_agregar (request):
    return render (request, 'pcracks/admin.html')

def admin_editar (request):
    return render (request, 'pcracks/admined.html')

def admin_eliminar (request):
    return render (request, 'pcracks/adminel.html')

def cuenta (request):
    return render (request, 'pcracks/cuenta.html')

def carrito (request):
    return render (request, 'pcracks/carrito.html')




def menu_fast_on_ram (request):
    return render (request, 'pcracks/menuFastONRam.html')

def menu_fast_on_procesador (request):
    return render (request, 'pcracks/menuFastONProcesador.html')

def menu_fast_on_placa (request):
    return render (request, 'pcracks/menuFastONPlaca.html')

def menu_fast_on_perifericos (request):
    return render (request, 'pcracks/menuFastONPerifericos.html')

def menu_fast_on_gpu (request):
    return render (request, 'pcracks/menuFastONGpu.html')

def menu_fast_on_gabinete (request):
    return render (request, 'pcracks/menuFastONGabinete.html')

def menu_fast_on_fuente (request):
    return render (request, 'pcracks/menuFastONFuente.html')

def menu_fast_on_almacenamiento (request):
    return render (request, 'pcracks/menuFastONAlmacenamiento.html')

def menu_fast_off_ram (request):
    return render (request, 'pcracks/menuFastOFFRam.html')

def menu_fast_off_procesador (request):
    return render (request, 'pcracks/menuFastOFFProcesador.html')

def menu_fast_off_placa (request):
    return render (request, 'pcracks/menuFastOFFPlaca.html')

def menu_fast_off_perifericos (request):
    return render (request, 'pcracks/menuFastOFFPerifericos.html')

def menu_fast_off_gpu (request):
    return render (request, 'pcracks/menuFastOFFGpu.html')

def menu_fast_off_gabinete (request):
    return render (request, 'pcracks/menuFastOFFGabinete.html')

def menu_fast_off_fuente (request):
    return render (request, 'pcracks/menuFastOFFFuente.html')

def menu_fast_off_almacenamiento (request):
    return render (request, 'pcracks/menuFastOFFAlmacenamiento.html')

