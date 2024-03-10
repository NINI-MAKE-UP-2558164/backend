from django import forms
from app1.models import Usuarios, empleados, ProductosRegistro


class UsuariosForm(forms.ModelForm):
    class Meta:
        model = Usuarios
        fields = ['nombres', 'apellidos', 'celular', 'email', 'direccion', 'contrasena']

class empleadosForm(forms.ModelForm):
    class Meta:
        model = empleados
        fields = ['nombres', 'apellidos', 'email', 'celular', 'genero','contrasena']
class productosRegistroForm(forms.ModelForm):
    class meta:
        model = ProductosRegistro
        fields = ['nombre', 'cantidad', 'precio', 'imagen']