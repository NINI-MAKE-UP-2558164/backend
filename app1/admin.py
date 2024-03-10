from django.contrib import admin
from app1.models import Usuarios, empleados, ProductosRegistro

@admin.register(Usuarios)
class UsuariosAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombres', 'apellidos', 'celular', 'email', 'direccion', 'contrasena','created_at','estado_usuarios_id')
@admin.register(empleados)
class empleadosAdmin(admin.ModelAdmin):
    list_display = ('id','nombres', 'apellidos', 'email', 'celular', 'genero', 'contrasena', 'cargo_id', 'estado_empleados_id')
@admin.register(ProductosRegistro)
class ProductosRegistro(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'precio', 'cantidad', 'imagen')


