from django.contrib import admin
from django.urls import include, path
# from proyecto.views import crear_empleados, editar_empleados, eliminar_empleados, empleados_1, lista_empleados
# from proyecto.views import inicio, registro, valida_login, lista_usuarios, crear_usuario, editar_usuario, eliminar_usuario, empleados, registro_empleados,user_logout

urlpatterns = [

    # # url empleados
    # path('admin/', admin.site.urls),
    
    # # url pagina principal
    # path('inicio/', inicio, name='inicio'),

    # # registro usuarios
    # path('registro/', registro, name='registro'),
    
    # # url crud de usuarios
    # path('lista_usuarios/', lista_usuarios, name='lista_usuarios'),
    # path('crear_usuario/', crear_usuario, name='crear_usuario'),
    # path('editar_usuario/<int:pk>/', editar_usuario, name='editar_usuario'),
    # path('eliminar_usuario/<int:pk>/', eliminar_usuario, name='eliminar_usuario'),
    
    # # url login usuarios
    # path('valida_login/', valida_login, name='valida_login'),
    
    # # url login empleados
    # path('empleados_1/', empleados_1, name='empleados_1'),

    # # url registro addministrador
    # path('registro_empleados/', registro_empleados, name='registro_empleados'),   

    # #  url de crud para empleados
    # path('empleados/', lista_empleados, name='lista_empleadoses'),
    # path('empleados/crear/', crear_empleados, name='crear_empleados'),
    # path('empleados/editar/<int:pk>/', editar_empleados, name='editar_empleados'),
    # path('empleados/eliminar/<int:pk>/', eliminar_empleados, name='eliminar_empleados'),
    # # logout
    # path('logout/', user_logout, name='logout'),
    
    # apirest
    
    path('', include ('app1.urls'))


    
    
]