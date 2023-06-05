from rest_framework import serializers
from pcracks.models import Cliente, Empleado
class ClienteSerializers(serializers.ModelSerializer):
    class Meta:
        model= Cliente
        fields = ['rut_cliente', 
                'nombre_cliente' ,
                'apellido_cliente' , 
                'direccion_cliente' ,
                'email_cliente' , 
                'num_telefonico_cliente' ,
                'contrasena_cliente' ]

class EmpleadoSerializers(serializers.ModelSerializer):
    class Meta :
        model= Empleado
        fields = ['rut_empleado',
                'nombre_empleado',
                'apellido_empleado',
                'direccion_empleado',
                'email_empleado',
                'cargo_empleado',
                'num_telefonico_empleado']