from django.db import models

class Usuarios(models.Model):
    id = models.AutoField(primary_key=True)
    nombres = models.CharField(max_length=254)
    apellidos = models.CharField(max_length=255)
    celular = models.BigIntegerField()
    email = models.CharField(max_length=254)
    direccion = models.CharField(max_length=254)
    contrasena = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    estado_usuarios_id = models.IntegerField(default=1)

    class Meta:
        managed = False
        db_table = 'usuarios'


class empleados(models.Model):
    id = models.AutoField(primary_key=True)
    nombres = models.CharField(max_length=254)
    apellidos = models.CharField(max_length=255)
    email = models.CharField(max_length=254)
    celular = models.BigIntegerField()
    genero = models.CharField(max_length=255)
    contrasena = models.CharField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)
    cargo_id = models.IntegerField(default=1)
    estado_empleados_id = models.IntegerField(default=1)
    

    class Meta:
        managed = False
        db_table = 'empleados'



class ProductosRegistro(models.Model):
    nombre = models.CharField(max_length=250)
    cantidad = models.IntegerField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    imagen = models.ImageField(upload_to='productos/', null=True, blank=True)
    create_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        managed = True
        db_table = 'productos_registro'



class TipoProducto(models.Model):
    tipo = models.CharField(max_length=45, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    update_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tipo_producto'

       


from rest_framework import serializers
from .models import ProductosRegistro

class ProductosRegistroSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductosRegistro
        fields = '__all__'


class Pgr(models.Model):
    tipo = models.CharField(max_length=45, blank=True, null=True)
    nombres_completos = models.CharField(max_length=45, blank=True, null=True)
    correo = models.CharField(max_length=45, blank=True, null=True)
    descripcion = models.CharField(max_length=45, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pgr'

# class Carousel(models.Model):
#     idcarousel = models.AutoField(primary_key=True)
#     nombre = models.CharField(max_length=100, blank=True, null=True)
#     descripcion = models.TextField(blank=True, null=True)
#     imagen_url = models.CharField(max_length=255, blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'carousel'