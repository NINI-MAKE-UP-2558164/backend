from rest_framework import serializers
from app1.models import ProductosRegistro,TipoProducto

class ProductosRegistroSerializer(serializers.ModelSerializer):
    class Meta: 
        model = ProductosRegistro
        fields = ['nombre', 'cantidad', 'precio']
        read_only_fields = ('create_at', )

    def validate_nombres(self, value):
        if len(value) < 3:
            raise serializers.ValidationError('Los nombres deben tener al menos 3 caracteres')
        return value

    def validate_cantidad(self, value):
        # Asegúrate de que 'value' sea un entero antes de comparar
        try:
            cantidad = int(value)
        except ValueError:
            raise serializers.ValidationError("La cantidad debe ser un número entero.")

        # Ahora puedes comparar 'cantidad' como un entero
        if cantidad < 0:
            raise serializers.ValidationError("La cantidad debe ser mayor o igual a cero.")

        return cantidad
    
class TipoProductoSerializer(serializers.ModelSerializer):
    class Meta: 
        model = ProductosRegistro
        fields = ['tipo']
        read_only_fields = ('create_at', )

