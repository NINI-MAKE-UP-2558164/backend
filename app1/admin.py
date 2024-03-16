from django.contrib import admin
from app1.models import Usuarios, empleados, ProductosRegistro, Pgr

@admin.register(Usuarios)
class UsuariosAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombres', 'apellidos', 'celular', 'email', 'direccion', 'contrasena', 'created_at', 'estado_usuarios_id')

@admin.register(empleados)
class empleadosAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombres', 'apellidos', 'email', 'celular', 'genero', 'contrasena', 'cargo_id', 'estado_empleados_id')

from django.contrib import admin
from app1.models import ProductosRegistro
from django.utils.html import format_html


@admin.register(ProductosRegistro)
class ProductosRegistroAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'precio', 'cantidad', 'imagen')

    readonly_fields = ['imagen_tag']

   
    def imagen_tag(self, obj):
        if obj.imagen:
            
            return format_html('<img src="{}" style="max-height: 200px; max-width: 200px;" />', obj.imagen.url)
        else:
            
            return '(Sin imagen)'

   
    imagen_tag.short_description = 'Vista previa de la imagen'


@admin.register(Pgr)
class PgrAdmin(admin.ModelAdmin):
    list_display = ('id', 'tipo', 'nombres_completos', 'correo', 'descripcion', 'created_at')
