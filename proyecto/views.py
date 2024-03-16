from django.http import JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib import messages
from django.contrib.auth.hashers import make_password,check_password
from django.views import View
from app1.models import ProductosRegistro, Usuarios, empleados
from app1.forms import UsuariosForm, empleadosForm
from django.shortcuts import render, redirect, get_object_or_404
from app1.models import empleados
from app1.models import TipoProducto


# nombre usuario en index


# logout
def user_logout(request):
   
    return render(request, 'index.html')



# index


def inicio(request):
    # Otras operaciones si es necesario
    return render(request, 'index.html')



# registro

def registro(request):
    if request.method == 'POST':
        nombres = request.POST.get('nombres')
        apellidos = request.POST.get('apellidos')
        celular = request.POST.get('celular')
        email = request.POST.get('email')
        direccion = request.POST.get('direccion')
        contrasena = request.POST.get('contrasena')

        # Validar que el campo 'celular' contenga solo números
        if not celular.isdigit():
            messages.error(request, 'El número de celular debe contener solo dígitos.')
            return redirect('registro')

        # Hashear la contraseña antes de guardarla en la base de datos
        contrasena_hasheada = make_password(contrasena)

        # Crear un nuevo usuario con los datos proporcionados
        nuevo_usuario = Usuarios(nombres=nombres, apellidos=apellidos, celular=celular, email=email, direccion=direccion, contrasena=contrasena_hasheada)
        nuevo_usuario.save()

        
        nuevo_usuario = Usuarios(nombres=nombres, apellidos=apellidos, celular=celular, email=email)
        registration_successful = True

        if registration_successful:
            messages.success(request,'¡Usuario registrado exitosamente!')
            return render(request, 'index.html')
    else:
        messages.warning(request, '¡Ya estás registrado!')
        return render(request, 'registro.html')



    
#  crud completo 



def lista_usuarios(request):
    usuarios = Usuarios.objects.all()
    return render(request, 'lista_usuarios.html', {'usuarios': usuarios})

def crear_usuario(request):
    if request.method == 'POST':
        form = UsuariosForm(request.POST)
        if form.is_valid():
            # Obtenemos la contraseña sin cifrar del formulario
            contrasena = form.cleaned_data['contrasena']
            
            # Usamos make_password para cifrar la contraseña
            contrasena_hasheada = make_password(contrasena)
            
            # Asignamos la contraseña cifrada al formulario
            form.cleaned_data['contrasena'] = contrasena_hasheada
            
            # Guardamos el formulario
            form.save()
            
            return redirect('lista_usuarios')
    else:
        form = UsuariosForm()
    return render(request, 'crear_usuario.html', {'form': form})


def editar_usuario(request, pk):
    usuario = get_object_or_404(Usuarios, pk=pk)
    if request.method == 'POST':
        form = UsuariosForm(request.POST, instance=usuario)
        if form.is_valid():
            form.save()
            return redirect('lista_usuarios')
    else:
        form = UsuariosForm(instance=usuario)
    return render(request, 'editar_usuario.html', {'form': form, 'usuario': usuario})

def eliminar_usuario(request, pk):
    usuario = get_object_or_404(Usuarios, pk=pk)
    if request.method == 'POST':
        usuario.delete()
        return redirect('lista_usuarios')
    return render(request, 'confirmar_eliminar.html', {'usuario': usuario})



# login


from django.contrib.auth.hashers import check_password
from django.contrib import messages
from django.shortcuts import render


def valida_login(request):
    if request.method == 'POST':
        usu = request.POST.get('email')
        contra = request.POST.get('contrasena')
     
        if Usuarios.objects.filter(email=usu).exists():
            logueo = Usuarios.objects.get(email=usu)
            passw = check_password(contra, logueo.contrasena)
            
            if passw:
                request.session['seguridad'] = True
                return render(request, 'inicio_sesion/index.html')
            else:
                messages.error(request, 'Usuario o contraseña incorrecta')
                return render(request, 'login.html')
        else:
            messages.error(request, 'Usuario no encontrado')
            return render(request, 'login.html')
    
    return render(request, 'login.html')

    

# Vista para listar todos los usuarios

def listar_usuarios(request):
    usuarios = Usuarios.objects.all()
    return render(request, 'listar_usuarios.html', {'usuarios': usuarios})

# Vista para eliminar un usuario

def eliminar_usuario(request, pk):
    usuario = get_object_or_404(Usuarios, pk=pk)
    if request.method == 'POST':
        usuario.delete()
        return redirect('lista_usuarios')
    return render(request, 'eliminar_usuario.html', {'usuario': usuario})

# login empleados



def empleados_1(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        contrasena = request.POST.get('contrasena')

        try:
            empleado = empleadosForm.objects.get(email=email)
        except empleados_1.DoesNotExist:
            messages.error(request, 'Usuario o contraseña incorrecta')
            return render(request, 'empleados/inicio_sesion.html')

        if check_password(contrasena, empleado.contrasena):  
            request.session['seguridad'] = True
            messages.success(request, 'Bienvenido empleados')
            return redirect('nombre_de_tu_vista')  # Reemplaza 'nombre_de_tu_vista' con el nombre correcto de tu vista
        else:
            messages.error(request, 'Usuario o contraseña incorrecta')
            return render(request, 'empleados/inicio_sesion.html')

    return render(request, 'empleados/inicio_sesion.html')


#  registro empleados
def registro_empleados(request):
    if request.method == 'POST':
        nombres = request.POST.get('nombres')
        apellidos = request.POST.get('apellidos')
        email = request.POST.get('email')
        celular = request.POST.get('celular')
        genero = request.POST.get('genero')
        contrasena = request.POST.get('contrasena')

        # Hash de la contraseña antes de guardarla en la base de datos
        contrasena_hasheada = make_password(contrasena)

        # Realiza la validación de datos aquí (si es necesario)

        # Crea un nuevo empleados con los datos proporcionados
        nuevo_empleados = empleados(
            nombres=nombres,
            apellidos=apellidos,
            email=email,
            celular=celular,
            genero=genero,
            contrasena=contrasena_hasheada
        )
        nuevo_empleados.save()

        messages.success(request, '¡Usuario registrado exitosamente!')
        return render(request, 'empleados/inicio_sesion.html')
    else:
        
        messages.success(request, '¡ya estas registrado!')
        return render(request, 'empleados/registro.html')
    


    

    # Lista de empleadoses
def lista_empleados(request):
    empleadoses = empleados.objects.all()
    return render(request, 'lista_usuarios.html', {'empleados': empleadoses})

# Crear empleados
def crear_empleados(request):
    if request.method == 'POST':
        form = empleados(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_empleados')
    else:
        form = empleados()
    return render(request, 'crud_empleados/crear_empleados.html', {'form': form})

# Editar empleados

def editar_empleados(request, pk):
    empleados = empleados.objects.get(pk=pk)
    if request.method == 'POST':
        form = empleados(request.POST, instance=empleados)
        if form.is_valid():
            form.save()
            return redirect('lista_usuarios.html')
    else:
        form = empleados(instance=empleados)
    return render(request, 'crud_empleados/editar_empleados.html', {'form': form, 'empleados': empleados})

# Eliminar empleados
def eliminar_empleados(request, pk):
    empleados = empleados.objects.get(pk=pk)
    if request.method == 'POST':
        empleados.delete()
        return redirect('lista_usuarios.html')
    return render(request, 'crud_empleados/confirmar_eliminar_empleados.html', {'empleados': empleados})


 # productos rest framework

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from app1.models import ProductosRegistro,TipoProducto
from app1.serializers import ProductosRegistroSerializer,TipoProductoSerializer

class ProductosRegistroViewSet(APIView):
    def get(self, request, *args, **kwargs):
        productos = ProductosRegistro.objects.all()
        serializer = ProductosRegistroSerializer(productos, many=True)
        return Response({'message': 'Success', 'productos': serializer.data}, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        serializer = ProductosRegistroSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = ProductosRegistroSerializer(instance, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



from rest_framework import viewsets

class ProductosRegistroModelViewSet(viewsets.ModelViewSet):
    queryset = ProductosRegistro.objects.all()
    serializer_class = ProductosRegistroSerializer

class TipoProductoViewSet(viewsets.ModelViewSet):
    queryset = TipoProducto.objects.all()
    serializer_class = TipoProductoSerializer
