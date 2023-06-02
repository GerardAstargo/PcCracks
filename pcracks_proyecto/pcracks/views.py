from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.hashers import check_password
from django.contrib.auth import authenticate,login, logout



# Create your views here.
def menu_off (request):
    return render(request, 'pcracks/menuOFF.html')



def buscar(request):
    if request.GET["barra_buscar"]:
        mensaje="Articulo buscado: %r" %request.GET["barra_buscar"]
        prd=request.GET["barra_buscar"]
        articulos=Producto.objects.filter(marca__icontains=prd)
        return render(request, "pcracks/resultados_busqueda.html", {"articulos": articulos, "query":prd})

    else:
        mensaje="no has introducido nada"
    return HttpResponse(mensaje)

def registro (request):
    
    return render(request, 'pcracks/registro.html')

def modificarCuenta (request):
    rutC = request.POST['rut']
    nombreC = request.POST['nombre']
    apellidoC = request.POST['apellido']
    direccionC = request.POST['direccion']
    emailC =  request.POST['correo']
    numeroC = request.POST['telefono']
    contrasenaC = request.POST['password']

    cliente = Cliente.objects.get(rut_cliente = rutC)
    cliente.nombre_cliente = nombreC
    cliente.apellido_cliente = apellidoC
    cliente.direccion_cliente = direccionC
    cliente.email_cliente = emailC
    cliente.num_telefonico_cliente = numeroC
    cliente.contrasena_cliente = contrasenaC

    cliente.save()
    messages.success(request,"Modificación realizada correctamente!")

    return redirect('cuenta')

def modificar (request, id):
    cliente = Cliente.objects.get(rut_cliente = id)
    contexto = {
        "datos": cliente
    }
    
    return render(request, 'pcracks/modificar_cuenta.html', contexto)


def agregarCliente(request):

    rutC = request.POST['rut']
    nombreC = request.POST['nombre']
    apellidoC = request.POST['apellido']
    direccionC = request.POST['direccion']
    emailC =  request.POST['correo']
    numeroC = request.POST['telefono']
    contrasenaC = request.POST['password']


    

    Cliente.objects.create(rut_cliente = rutC, nombre_cliente = nombreC,
                           apellido_cliente = apellidoC, direccion_cliente = direccionC,
                           email_cliente = emailC, num_telefonico_cliente = numeroC,
                           contrasena_cliente = contrasenaC)
    user=User.objects.create_user(
        username= emailC,
        email = emailC,
        password = contrasenaC
)
    user.is_staff = True
    user.save()
    messages.success(request,"Cuenta creada correctamente!")
    return redirect('login')


def menu_on (request):
    return render (request, 'pcracks/menuON.html')

def mapa_off (request):
    return render (request, 'pcracks/mapaOFF.html')

def mapa_on (request):
    return render (request, 'pcracks/mapaON.html')

def login (request):
    usuario1 = request.POST['correo']
    contra1 = request.POST['password']

    try:
        user1 = User.objects.get(email = usuario1)
    except User.DoesNotExist:
        messages.error(request,'El correo o la contraseña son incorrectas')
        return redirect('login')

    pass_valida = check_password(contra1, user1.password)
    if not pass_valida:
        messages.error(request,'El correo o la contraseña son incorrectas')
        return redirect('login')

    usuario2 = Cliente.objects.get(email_empleado = usuario1,rut_empleado=contra1)
    user = authenticate(email=usuario1, password=contra1)

    if user is not None:
        login(request, user)
        if (usuario2.tipousuario.idTipoUsuario == 1):
            return redirect ('admin')
        else:
            contexto = {"usuario":usuario2}
    else:
        messages.error(request,'Cuenta invalida')
    return render (request, 'pcracks/menuON.html',contexto)

def recuperarContrasena (request):

    return render (request, 'pcracks/recuperarContrasena.html')

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
    
    cuenta = Cliente.objects.all()
    contexto ={
        "listaCliente": cuenta
    }

    return render (request, 'pcracks/cuenta.html', contexto)

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

