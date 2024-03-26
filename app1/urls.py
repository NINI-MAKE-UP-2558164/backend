from rest_framework import routers
from .api import ProductosRegistroViewsSet, TipoProductoViewSet, PqrViewSet, EmpleadosViewSet, UsuariosViewSet
from django.urls import path

router = routers.DefaultRouter()
router.register('api/app1/productos', ProductosRegistroViewsSet, 'productos')
router.register('api/app1/tipos', TipoProductoViewSet, 'tipos')
router.register('api/app1/pqr', PqrViewSet, 'pqr')
router.register('api/app1/empleados', EmpleadosViewSet, 'empleados' )
router.register('api/app1/Usuarios', UsuariosViewSet, 'Usuarios' )


urlpatterns = router.urls
