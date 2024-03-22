from django import forms
from app1.models import Usuarios, empleados, ProductosRegistro,Pqr


class UsuariosForm(forms.ModelForm):
    class Meta:
        model = Usuarios
        fields = ['nombres', 'apellidos', 'celular', 'email', 'direccion', 'contrasena']

class empleadosForm(forms.ModelForm):
    class Meta:
        model = empleados
        fields = ['nombres', 'apellidos', 'email', 'celular', 'genero','contrasena']
class productosRegistroForm(forms.ModelForm):
    class Meta:  
        model = ProductosRegistro
        fields = ['nombre', 'cantidad', 'precio', 'imagen']

class PqrForm(forms.ModelForm):
    class Meta:
        model = Pqr
        fields = ['tipo', 'nombres_completos', 'correo', 'descripcion', 'created_at']