from rest_framework import serializers
from app1.models import ProductosRegistro, TipoProducto, Pqr, Usuarios, Empleados


# productos_registro
class ProductosRegistroSerializer(serializers.ModelSerializer):
    class Meta: 
        model = ProductosRegistro
        fields = ['nombre', 'precio', 'cantidad', 'imagen', 'created_at']
        read_only_fields = ('created_at', )

    def validate_nombre(self, value):
        if len(value) < 3:
            raise serializers.ValidationError('Los nombres deben tener al menos 3 caracteres')
        return value

    def validate_cantidad(self, value):
        try:
            cantidad = int(value)
        except ValueError:
            raise serializers.ValidationError("La cantidad debe ser un número entero.")

        if cantidad < 0:
            raise serializers.ValidationError("La cantidad debe ser mayor o igual a cero.")

        return cantidad
    
# tipoproducto    
class TipoProductoSerializer(serializers.ModelSerializer):
    class Meta: 
        model = TipoProducto
        fields = ['tipo', 'created_at']
        read_only_fields = ('created_at', )

# pqr
class PqrSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pqr
        fields = ['tipo', 'nombres_completos', 'correo', 'descripcion', 'created_at']
        read_only_fields = ('created_at', )



# empleados
class EmpleadosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Empleados
        fields = '__all__'

# usuarios
class UsuariosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuarios
        fields = '__all__'

