from django.db import models


# usuarios
class Usuarios(models.Model):
    id = models.AutoField(primary_key=True)
    nombres = models.CharField(max_length=254)
    apellidos = models.CharField(max_length=255)
    celular = models.BigIntegerField()
    email = models.CharField(max_length=254)
    direccion = models.CharField(max_length=254)
    contrasena = models.CharField(max_length=255)
    estado_usuarios_id = models.IntegerField(default=1)
    created_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'usuarios'

# empleados
class Empleados(models.Model):
    nombres = models.CharField(max_length=45, blank=True, null=True)
    apellidos = models.CharField(max_length=45, blank=True, null=True)
    email = models.CharField(max_length=45, blank=True, null=True)
    celular = models.CharField(max_length=45, blank=True, null=True)
    genero = models.CharField(max_length=45, blank=True, null=True)
    contrasena = models.CharField(max_length=450, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    cargo_id = models.IntegerField()
    estado_empleados_id = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'empleados'
        unique_together = (('id', 'cargo_id', 'estado_empleados_id'),)



# tipoproducto
class TipoProducto(models.Model):
    tipo = models.CharField(max_length=45, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tipo_producto'

# productos_registro
class ProductosRegistro(models.Model):
    nombre = models.CharField(max_length=45, blank=True, null=True)
    precio = models.CharField(max_length=45, blank=True, null=True)
    cantidad = models.CharField(max_length=45, blank=True, null=True)
    imagen = models.ImageField(upload_to='img/productos', blank=True)
    created_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'productos_registro'
       

# pqr
class Pqr(models.Model):
    tipo = models.CharField(max_length=45, blank=True, null=True)
    nombres_completos = models.CharField(max_length=45, blank=True, null=True)
    correo = models.CharField(max_length=45, blank=True, null=True)
    descripcion = models.CharField(max_length=45, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pqr'


        


