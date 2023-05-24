from django.contrib import admin

from pcracks.models import Cliente, Producto, Empleado, Compra, Pedido, Foto, Contacto, Usuario
# Register your models here.
class ClientesAdmin(admin.ModelAdmin):
    list_display = ("nombre_cliente", "rut_cliente", "email_cliente", "direccion_cliente")
    search_fields = ("nombre_cliente", "rut_cliente")

class ProductosAdmin(admin.ModelAdmin):
    list_filter = ("marca",)

"""
class PedidosAdmin(admin.ModelAdmin):
    list_display = ("cod_pedido" ,"fecha") 
    search_fields = ("cod_pedido")
    list_filter = ("fecha",)
    date_hierarchy = "fecha"
"""

admin.site.register(Cliente, ClientesAdmin)
admin.site.register(Producto, ProductosAdmin)
admin.site.register(Empleado)
admin.site.register(Compra)
admin.site.register(Pedido)
admin.site.register(Foto)
admin.site.register(Contacto)
admin.site.register(Usuario)
