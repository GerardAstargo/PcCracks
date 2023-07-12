from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.hashers import check_password
from django.contrib.auth import authenticate,login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import AnonymousUser 
from pcracks.CarritoConf import Carrito



# Create your views here.
def menu_off (request):
    return render(request, 'pcracks/menuOFF.html')
def plantillaON (request):
    return render(request, 'pcracks/zplantillaON.html')




def logout_request (request):
    num=0
    if num < 0:
        logout(request)
        counter += 1
        logout_request(num - 1)
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

def producto (request):
    
    return render(request, 'pcracks/agregar_producto.html')

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

def modificarProductoadmin (request):
    codP = request.POST['rut']
    marcaP = request.POST['nombre']
    modeloP = request.POST['apellido']
    descripcionP = request.POST['direccion']
    disponibilidadP =  request.POST['correo']
    precioP = request.POST['telefono']
    categoriaP = request.POST['password']

    producto = Producto.objects.get(cod_producto = codP)
    producto.marca = marcaP
    producto.modelo = modeloP
    producto.descripcion = descripcionP
    producto.disponibilidad = disponibilidadP
    producto.precio = precioP
    producto.categoria = categoriaP

    Producto.save()
    messages.success(request,"Modificación realizada correctamente!")

    return redirect('adminProductos')


def modificarProducto (request, id):
    producto = Producto.objects.get(cod_producto = id)
    contexto = {
        "dato": producto
    }
    
    return render(request, 'pcracks/modificar_producto.html', contexto)

def comprarProducto (request):
    codP = request.POST['rut']
    marcaP = request.POST['nombre']
    modeloP = request.POST['apellido']
    descripcionP = request.POST['direccion']
    disponibilidadP =  request.POST['correo']
    precioP = request.POST['telefono']
    categoriaP = request.POST['password']

    producto = Producto.objects.get(cod_producto = codP)
    producto.marca = marcaP
    producto.modelo = modeloP
    producto.descripcion = descripcionP
    producto.disponibilidad = disponibilidadP
    producto.precio = precioP
    producto.categoria = categoriaP


    return redirect('cuenta')

def comprar (request, id):
    producto = Producto.objects.get(cod_producto = id)
    contexto = {
        "listaProducto": producto
    }
    
    return render(request, 'pcracks/PRODUCTOS/CPU/i511th.html', contexto)

def eliminarUsuario (request, id):
    cliente = Cliente.objects.get(rut_cliente = id)
    cliente.delete()
    return redirect('adminUsuarios')


def eliminarProducto (request, id):
    producto = Producto.objects.get(cod_producto = id)
    producto.delete()
    return redirect('adminProductos')


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

        username= nombreC,
        email = emailC,
        password = contrasenaC
)
    user.is_staff = False
    user.save()
    messages.success(request,"Cuenta creada correctamente!")
    return redirect('registro')

def agregarProducto(request):

    codP = request.POST['codigo']
    marcaP = request.POST['marca']
    modeloP = request.POST['modelo']
    descripcionP = request.POST['descripcion']
    disponibilidadP =  request.POST['disponibilidad']
    precioP = request.POST['precio']
    categoriaP = request.POST['categoria']


    

    Producto.objects.create(cod_producto = codP, marca = marcaP,
                           modelo = modeloP, descripcion = descripcionP,
                           disponibilidad = disponibilidadP, precio = precioP,
                           categoria = categoriaP)

    messages.success(request,"Producto agregado correctamente!")
    return redirect('adminProductos')


def menu_on (request):
    
    return render (request, 'pcracks/menuON.html')

def mapa_off (request):
    return render (request, 'pcracks/mapaOFF.html')

def contacto (request):
    emailC =  request.POST['email']
    nombreC = request.POST['nombre']
    mensajeC = request.POST['message']

    Contacto.objects.create(correo= emailC ,nombre = nombreC, mensaje=mensajeC
                           )
    return redirect('mapa_on')

def mapa_on (request):

    return render (request, 'pcracks/mapaON.html')

def login (request):
    return render (request, 'pcracks/Login.html')

def inicioSesion (request):
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

    user = authenticate(email=usuario1, password=contra1)

    if user is not None:
        user.is_authenticated = True
        login(request, user)
        

    return render (request, 'pcracks/menuON.html')
        


def recuperarContrasena (request):

    return render (request, 'pcracks/recuperarContrasena.html')

def menu_off_productos (request):
    productos = Producto.objects.all()
    contexto ={
        "listaProducto": productos
    }
    return render (request, 'pcracks/menuOFFproductos.html', contexto)

def menu_on_productos (request):
    productos = Producto.objects.all()
    contexto ={
        "listaProducto": productos
    }
    return render (request, 'pcracks/menuONproductos.html',contexto)

def administrar (request):
    return render (request, 'pcracks/administrar.html')

def adminProductos(request):

    productos = Producto.objects.all()
    contexto ={
        "listaProducto": productos
    }

    return render (request, 'pcracks/administrar_productos.html',contexto)

def adminUsuarios (request):

    cuenta = Cliente.objects.all()
    contexto ={
        "listaCliente": cuenta
    }

    return render (request, 'pcracks/administrar_usuarios.html', contexto)


def cuenta (request):

            cuenta = Cliente.objects.all()
            contexto ={
            "listaCliente": cuenta
            }
            return render(request, 'pcracks/cuenta.html', contexto)

        

        

    

def cuentaoff (request):
   return render (request, 'pcracks/cuentaoff.html')



def agregar_producto_carrito(request, id):
    carrito = Carrito(request)
    producto = Producto.objects.get(cod_producto = id)
    carrito.agregar(producto)
    return redirect("carritoCompra")

def eliminar_producto_carrito(request, id):
    carrito = Carrito(request)
    producto = Producto.objects.get(cod_producto = id)
    carrito.eliminar(producto)
    return redirect("carritoCompra")

def restar_producto_carrito(request, id):
    carrito = Carrito(request)
    producto = Producto.objects.get(cod_producto = id)
    carrito.restar(producto)
    return redirect("carritoCompra")

def limpiar_carrito (request):
    carrito = Carrito(request)
    carrito.limpiar()
    return redirect("carritoCompra")

def carritoCompra (request):
    productos = Producto.objects.all()
    contexto ={
        "listaProducto": productos
    }

    return render (request, 'pcracks/carrito.html',contexto)




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

