from .models import ProductosRegistro,TipoProducto
from rest_framework import viewsets, permissions
from .serializers import ProductosRegistroSerializer,TipoProductoSerializer

class ProductosRegistroViewsSet(viewsets.ModelViewSet):
    queryset = ProductosRegistro.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = ProductosRegistroSerializer 


class TipoProductoViewSet(viewsets.ModelViewSet):
    queryset = TipoProducto.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = TipoProductoSerializer  



from rest_framework import viewsets
from rest_framework.response import Response
from .models import Pgr
from .serializers import PgrSerializer

class PgrViewSet(viewsets.ModelViewSet):
    queryset = Pgr.objects.all()
    serializer_class = PgrSerializer
