from .models import ProductosRegistro,TipoProducto
from rest_framework import viewsets, permissions
from .serializers import ProductosRegistroSerializer,TipoProductoSerializer

class ProductosRegistroViewsSet(viewsets.ModelViewSet):
    queryset = ProductosRegistro.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = ProductosRegistroSerializer  # Corregido el nombre de la propiedad


class TipoProductoViewSet(viewsets.ModelViewSet):
    queryset = TipoProducto.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = TipoProductoSerializer  # Corregido el nombre de la propiedad
