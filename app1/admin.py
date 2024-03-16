from django.contrib import admin
from app1.models import ProductosRegistro, Pqr

# @admin.register(Usuarios)
# class UsuariosAdmin(admin.ModelAdmin):
#     list_display = ('id', 'nombres', 'apellidos', 'celular', 'email', 'direccion', 'contrasena', 'created_at', 'estado_usuarios_id')

# @admin.register(empleados)
# class empleadosAdmin(admin.ModelAdmin):
#     list_display = ('id', 'nombres', 'apellidos', 'email', 'celular', 'genero', 'contrasena', 'cargo_id', 'estado_empleados_id')

from django.contrib import admin
from app1.models import ProductosRegistro
from django.utils.html import format_html


@admin.register(ProductosRegistro)
class ProductosRegistroAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'precio', 'cantidad', 'imagen', 'created_at')

    readonly_fields = ['imagen_tag']

   
    def imagen_tag(self, obj):
        if obj.imagen:
            
            return format_html('<img src="{}" style="max-height: 200px; max-width: 200px;" />', obj.imagen.url)
        else:
            
            return '(Sin imagen)'

   
    imagen_tag.short_description = 'Vista previa de la imagen'


@admin.register(Pqr)
class PqrAdmin(admin.ModelAdmin):
    list_display = ('id', 'tipo', 'nombres_completos', 'correo', 'descripcion', 'created_at')



from django.contrib import admin
from .models import TipoProducto

@admin.register(TipoProducto)
class TipoProductoAdmin(admin.ModelAdmin):
    list_display = ('id', 'tipo', 'created_at')
    search_fields = ('tipo',)  # Campo de búsqueda para el tipo de producto
    readonly_fields = ('created_at',)  # Campo de fecha de creación como solo lectura

    fieldsets = (
        ('Información del Tipo', {
            'fields': ('tipo',)
        }),
        ('Fechas', {
            'fields': ('created_at',),
            'classes': ('collapse',)  # Oculta este campo por defecto
        }),
    )

    def get_readonly_fields(self, request, obj=None):
        if obj:  # Si es una instancia existente, deja el campo de fecha como solo lectura
            return self.readonly_fields
        return ()  # Si es una nueva instancia, no hay campos de solo lectura