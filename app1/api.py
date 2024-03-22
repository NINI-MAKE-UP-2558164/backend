from .models import ProductosRegistro, TipoProducto, Pqr, Usuarios, Empleados
from rest_framework import viewsets, permissions
from .serializers import ProductosRegistroSerializer,TipoProductoSerializer,PqrSerializer, UsuariosSerializer, EmpleadosSerializer

# productos_registro
class ProductosRegistroViewsSet(viewsets.ModelViewSet):
    queryset = ProductosRegistro.objects.all()
    print(queryset)
    permission_classes = [permissions.AllowAny]
    serializer_class = ProductosRegistroSerializer 

# tipoproducto
class TipoProductoViewSet(viewsets.ModelViewSet):
    queryset = TipoProducto.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = TipoProductoSerializer  

# pqr
class PqrViewSet(viewsets.ModelViewSet):
    queryset = Pqr.objects.all()
    serializer_class = PqrSerializer

# empleados
class EmpleadosViewSet(viewsets.ModelViewSet):
    queryset = Empleados.objects.all()
    serializer_class = EmpleadosSerializer

# usuarios
class UsuariosViewSet(viewsets.ModelViewSet):
    queryset = Usuarios.objects.all()
    serializer_class = UsuariosSerializer