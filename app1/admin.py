from django.contrib import admin
from app1.models import ProductosRegistro, Pqr, Empleados, TipoProducto, Usuarios
from django.utils.html import format_html

# usuarios
@admin.register(Usuarios)
class UsuariosAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombres', 'apellidos', 'celular', 'email', 'direccion', 'contrasena', 'estado_usuarios_id', 'created_at')

# empleados
@admin.register(Empleados)
class empleadosAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombres', 'apellidos', 'email', 'celular', 'genero', 'contrasena', 'cargo_id', 'estado_empleados_id', 'created_at')



# productos_registro
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



# admin pqr
@admin.register(Pqr)
class PqrAdmin(admin.ModelAdmin):
    list_display = ('id', 'tipo', 'nombres_completos', 'correo', 'descripcion', 'created_at')
    readonly_fields = ('created_at',) 



# tipoproducto
@admin.register(TipoProducto)
class TipoProductoAdmin(admin.ModelAdmin):
    list_display = ('id', 'tipo', 'created_at')
    search_fields = ('tipo',) 
    readonly_fields = ('created_at',)  
    fieldsets = (
        ('Información del Tipo', {
            'fields': ('tipo',)
        }),
        ('Fechas', {
            'fields': ('created_at',),
            'classes': ('collapse',)  
        }),
    )

    def get_readonly_fields(self, request, obj=None):
        if obj:  
            return self.readonly_fields
        return ()  