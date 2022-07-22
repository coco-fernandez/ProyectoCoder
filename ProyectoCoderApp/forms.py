from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class nuevo_estudio(forms.Form):
    nombre=forms.CharField(max_length=30,label="Nombre")
    ubicacion=forms.CharField(max_length=30,label="Ubicación")
    cantidad_salas=forms.IntegerField()
    
class nuevo_banda(forms.Form):
    nombre=forms.CharField(max_length=30,label="Nombre")
    genero=forms.CharField(max_length=30,label="Género")
    cantidad_integrantes=forms.IntegerField()
    
class nuevo_productor(forms.Form):
    nombre=forms.CharField(max_length=30,label="Nombre")
    apellido=forms.CharField(max_length=30,label="Apellido")
    email=forms.EmailField()
    


class UserEditForm(UserCreationForm):

    first_name = forms.CharField(label="Nombre")
    last_name = forms.CharField(label="Apellido")
    email = forms.EmailField(label="Email")
        
    password1 = forms.CharField(label="Ingrese contraseña", widget=forms.PasswordInput, required=False) # la contraseña no se vea
    password2 = forms.CharField(label="Reingrese contraseña", widget=forms.PasswordInput, required=False)

    class Meta:
        model = User
        fields = [ 'first_name', 'last_name','email', 'password1', 'password2']

        help_texts = {k:"" for k in fields}


roles = [("banda", "Banda"), ("productor", "Productor")]
class UserRegisterForm(UserCreationForm):
    
    first_name = forms.CharField(label="Nombre")
    last_name = forms.CharField(label="Apellido")
    email = forms.EmailField(label="Email")
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput) # la contraseña no se vea
    password2 = forms.CharField(label="Confirmar contraseña", widget=forms.PasswordInput)

    roles = forms.MultipleChoiceField(choices=roles, label="Roles", widget=forms.Select(choices=roles))


    class Meta:
        model = User
        fields = ['username','first_name', 'last_name', 'email', 'password1', 'password2', ]