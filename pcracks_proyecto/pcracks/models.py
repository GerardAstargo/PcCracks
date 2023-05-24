from django.db import models

# Create your models here.


#BASE CLIENTE
class Cliente(models.Model):
  rut_cliente = models.CharField(max_length=15, primary_key=True)
  nombre_cliente = models.CharField(max_length=15)
  fecha_nacimiento = models.DateField(blank=True, null=True)
  direccion_cliente = models.CharField(max_length=30)
  email_cliente = models.CharField(max_length=20)
  num_telefonico_cliente = models.IntegerField()
  
#BASE EMPLEADO
class Empleado (models.Model):
  rut_empleado = models.CharField(max_length=15, primary_key=True)
  nombre_empleado = models.CharField(max_length=15)
  fecha_nacimiento = models.DateField()
  direccion_empleado = models.CharField(max_length=30)
  email_empleado = models.CharField(max_length=20)
  num_telefonico_empleado = models.IntegerField()


#BASE COMPRA
class Compra(models.Model):
  compra_id = models.IntegerField(primary_key=True)
  metodo_pago = models.CharField(max_length=20)
  cantidad_productos = models.IntegerField()
  total_compra = models.IntegerField()
  fecha_compra = models.DateField()
  cliente = models.ForeignKey(Cliente,on_delete=models.CASCADE)

#BASE PRODUCTO
class Producto (models.Model):
  marca = models.CharField(max_length=20)
  modelo = models.CharField(max_length=20)
  precio = models.IntegerField(verbose_name="$")
  compra = models.ForeignKey(Compra,on_delete=models.CASCADE, blank=True, null=True)

  def __str__(self):
    return 'El producto de la marca %s, modelo %s tiene un precio de $%s y lo compro este cliente %s' %(self.marca, self.modelo, self.precio, self.compra)

#BASE PEDIDOS
class Pedido (models.Model):
  cod_pedido = models.IntegerField(primary_key=True)

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

