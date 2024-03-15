from rest_framework import routers
from .api import ProductosRegistroViewsSet, TipoProductoViewSet, PgrViewSet
from django.urls import path

router = routers.DefaultRouter()
router.register('api/app1/productos', ProductosRegistroViewsSet, 'productos')
router.register('api/app1/tipos', TipoProductoViewSet, 'tipos')
router.register('api/app1/pgr', PgrViewSet, 'pgr')

urlpatterns = router.urls
