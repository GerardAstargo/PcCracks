from django.contrib import admin

from pcracks.models import Cliente, Producto, Empleado, Compra, Pedido, Foto, Contacto, Usuario
# Register your models here.

admin.site.register(Cliente)
admin.site.register(Producto)
admin.site.register(Empleado)
admin.site.register(Compra)
admin.site.register(Pedido)
admin.site.register(Foto)
admin.site.register(Contacto)
admin.site.register(Usuario)
