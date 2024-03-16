from .models import ProductosRegistro,TipoProducto,Pqr
from rest_framework import viewsets, permissions
from .serializers import ProductosRegistroSerializer,TipoProductoSerializer,PqrSerializer

class ProductosRegistroViewsSet(viewsets.ModelViewSet):
    queryset = ProductosRegistro.objects.all()
    print(queryset)
    permission_classes = [permissions.AllowAny]
    serializer_class = ProductosRegistroSerializer 


class TipoProductoViewSet(viewsets.ModelViewSet):
    queryset = TipoProducto.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = TipoProductoSerializer  


class PqrViewSet(viewsets.ModelViewSet):
    queryset = Pqr.objects.all()
    serializer_class = PqrSerializer
