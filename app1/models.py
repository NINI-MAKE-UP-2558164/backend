from django.db import models

# class Usuarios(models.Model):
#     id = models.AutoField(primary_key=True)
#     nombres = models.CharField(max_length=254)
#     apellidos = models.CharField(max_length=255)
#     celular = models.BigIntegerField()
#     email = models.CharField(max_length=254)
#     direccion = models.CharField(max_length=254)
#     contrasena = models.CharField(max_length=255)
#     estado_usuarios_id = models.IntegerField(default=1)

#     class Meta:
#         managed = False
#         db_table = 'usuarios'


# class Empleados(models.Model):
#     nombres = models.CharField(max_length=45, blank=True, null=True)
#     apellidos = models.CharField(max_length=45, blank=True, null=True)
#     email = models.CharField(max_length=45, blank=True, null=True)
#     celular = models.CharField(max_length=45, blank=True, null=True)
#     genero = models.CharField(max_length=45, blank=True, null=True)
#     contrasena = models.CharField(max_length=450, blank=True, null=True)
#     created_at = models.DateTimeField(blank=True, null=True)
#     cargo_id = models.IntegerField()
#     estado_empleados_id = models.IntegerField()
#     update_at = models.DateTimeField(blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'empleados'
#         unique_together = (('id', 'cargo_id', 'estado_empleados_id'),)




class TipoProducto(models.Model):
    tipo = models.CharField(max_length=45, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tipo_producto'


from django.db import models



class ProductosRegistro(models.Model):
    nombre = models.CharField(max_length=250, blank=True, null=True)
    precio = models.CharField(max_length=250, blank=True, null=True)
    cantidad = models.CharField(max_length=250, blank=True, null=True)
    imagen = models.ImageField(upload_to='img/productos', blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'productos_registro'
       


from rest_framework import serializers
from .models import ProductosRegistro

class ProductosRegistroSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductosRegistro
        fields = '__all__'


class Pqr(models.Model):
    tipo = models.CharField(max_length=45, blank=True, null=True)
    nombres_completos = models.CharField(max_length=45, blank=True, null=True)
    correo = models.CharField(max_length=45, blank=True, null=True)
    descripcion = models.CharField(max_length=45, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pqr'


        


