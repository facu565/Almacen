from django.contrib import admin
from .models import *


# Register your models here.
class ClienteAdmin(admin.ModelAdmin):
    list_display = ['rut', 'nombre','telefono',]
    search_fields = ['nombre',]

class ProductoInline(admin.TabularInline):
    model = Producto

class ProveedorAdmin(admin.ModelAdmin):
    list_display = ['rut','nombre','telefono','web']
    list_filter = ['rut','nombre']
    inlines = [ProductoInline,]

class VentaAdmin(admin.ModelAdmin):
    list_display = ('id','cliente','descuento')
    actions = ['cambiar_descuento',]

    def cambiar_descuento (self, request, queryset):
        if Venta.descuento == False:
            return queryset.update(descuento=True)
        #return queryset.update(descuento=True)

#class ProductoAdmin(admin.ModelAdmin):


admin.site.register(Direccion)
admin.site.register(Categoria)
admin.site.register(Proveedor)
admin.site.register(Producto)
admin.site.register(Detalle)
admin.site.register(Cliente)
admin.site.register(Venta)
