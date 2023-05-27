from django.db import models

# Create your models here.


#BASE CLIENTE
class Cliente(models.Model):
  rut_cliente = models.CharField(max_length=15, primary_key=True)
  nombre_cliente = models.CharField(max_length=15)
  apellido_cliente = models.CharField(max_length=15)
  fecha_nacimiento = models.DateField(blank=True, null=True)
  direccion_cliente = models.CharField(max_length=30)
  email_cliente = models.CharField(max_length=20)
  num_telefonico_cliente = models.IntegerField()

  def __str__(self):
    return self.nombre_cliente
  
#BASE EMPLEADO
class Empleado (models.Model):
  rut_empleado = models.CharField(max_length=15, primary_key=True)
  nombre_empleado = models.CharField(max_length=15)
  apellido_empleado = models.CharField(max_length=15)
  fecha_nacimiento = models.DateField()
  direccion_empleado = models.CharField(max_length=30)
  email_empleado = models.CharField(max_length=20)
  cargo_empleado = models.CharField(max_length=20)
  num_telefonico_empleado = models.IntegerField()


#BASE COMPRA
class Compra(models.Model):
  compra_id = models.IntegerField(primary_key=True)
  metodo_pago = models.CharField(max_length=20)
  cantidad_productos = models.IntegerField()
  total_compra = models.IntegerField()
  fecha_compra = models.DateTimeField(auto_now_add=True)


#BASE PRODUCTO
class Producto (models.Model):
  cod_producto = models.IntegerField(primary_key=True)
  marca = models.CharField(max_length=20)
  modelo = models.CharField(max_length=20)
  descripcion = models.CharField(max_length=400)
  disponibilidad = models.IntegerField()
  precio = models.IntegerField(verbose_name="$")
  categoria = models.CharField(max_length=20)

  def __str__(self):
    return 'El producto de la marca %s, modelo %s tiene un precio de $%s y lo compro este cliente %s' %(self.marca, self.modelo, self.precio, self.compra)

#BASE PEDIDOS
class Pedido (models.Model):
  cod_pedido = models.IntegerField(primary_key=True)
  fecha_pedido = models.DateTimeField(auto_now_add=True)
  cliente = models.ForeignKey(Cliente,on_delete=models.CASCADE)

#BASE FOTOS
class Foto (models.Model):
  foto = models.ImageField(upload_to="producto")

#BASE CONTACTO
class Contacto (models.Model):
  correo = models.CharField(max_length=20)
  nombre = models.CharField(max_length=20)
  mensaje = models.CharField(max_length=300)

#BASE USUARIO
class Usuario(models.Model):
  correo_electronico = models.CharField(max_length=20)
  contrasena = models.CharField(max_length=20)

