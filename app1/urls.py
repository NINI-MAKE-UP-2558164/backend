from rest_framework import routers
from .api import ProductosRegistroViewsSet,TipoProductoViewSet
from django.urls import path

router = routers.DefaultRouter()
router.register('api/app1', ProductosRegistroViewsSet, 'app1'),
router.register('api/app1', TipoProductoViewSet, 'app1')
urlpatterns = router.urls