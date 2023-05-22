from django.db import models

# Create your models here.


#BASE CLIENTE
class Cliente(models.Model):
  rut_cliente = models.CharField(max_length=15, primary_key=True)
  nombre_cliente = models.CharField(max_length=15)
  fecha_nacimiento = models.DateField()
  direccion_cliente = models.CharField(max_length=30)
  email_cliente = models.CharField(max_length=20)
  num_telefonico_cliente = models.IntegerField()
  

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
  precio = models.IntegerField()
  compra = models.ForeignKey(Compra,on_delete=models.CASCADE)

#BASE EMPLEADO
class Empleado (models.Model):
  rut_empleado = models.CharField(max_length=15, primary_key=True)
  nombre_empleado = models.CharField(max_length=15)
  fecha_nacimiento = models.DateField()
  direccion_empleado = models.CharField(max_length=30)
  email_empleado = models.CharField(max_length=20)
  num_telefonico_empleado = models.IntegerField()