from django.db import models

# Create your models here.
"""
class Raza(models.Model):
    codigoRaza = models.AutoField(primary_key=True)
    nombreRaza= models.CharField(max_length=15)

class Mascota(models.Model):
  codigoChip = models.CharField(max_length=20, primary_key=True)
  nombreMascota = models.CharField(max_length=25,verbose_name='nombreDelaMascota')
  edadMascota = models.IntegerField()
  foto = models.ImageField(upload_to="mascotas")
  raza = models.ForeignKey(Raza,on_delete=models.CASCADE)
"""