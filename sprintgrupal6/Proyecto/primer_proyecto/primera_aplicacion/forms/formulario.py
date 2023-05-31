from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import Group



class RegistrationForm(UserCreationForm):
    group = forms.ModelChoiceField(queryset=Group.objects.all())

    class Meta(UserCreationForm.Meta):
        fields = UserCreationForm.Meta.fields + ('group',)


class FormularioSupplierForm(forms.Form):
    direccion = forms.CharField(max_length=50, label="Direccion", required=True, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Ingrese su direccion'}))
    area = forms.CharField(label="Area", required=True, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Ingrese su area'}))
    producto = forms.CharField(max_length=50, label="Producto", required=True, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Ingrese su producto'}))
    
class FormularioUsuarioForm(forms.Form):
    direccion = forms.CharField(max_length=50, label="Direccion", required=True, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Ingrese su direccion'}))
    edad = forms.IntegerField(label="Edad", required=True, widget=forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Ingrese su edad'}))
    profesion = forms.CharField(max_length=50, label="Profesion", required=True, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Ingrese su profesion'}))

class LoginForm(forms.Form):
    username = forms.CharField(max_length=50, label="Usuario", required=True, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Ingrese su usuario'}),
                               error_messages={'required': 'El Usuario es requerida'})
    password = forms.CharField(max_length=20, label="Contraseña", required=True, widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'Ingrese su contraseña'}),
                               error_messages={'required': 'La contraseña es requerida'})

class RegistrationForm(UserCreationForm):
    # Campos adicionales para el formulario de registro
    username = forms.CharField(max_length=20, required=True)
    password1 = forms.CharField(max_length=10, required=True)
    password2 = forms.CharField(max_length=10, required=True)
    first_name = forms.CharField(max_length=100, required=True)
    last_name = forms.CharField(max_length=100, required=True)
    email = forms.CharField(max_length=50, required=True)
    group = forms.ModelChoiceField(queryset=Group.objects.all())

    def __init__(self, *args, **kwargs):
        groups = kwargs.pop('groups', None)
        super().__init__(*args, **kwargs)
        if groups:
            self.fields['group'].queryset = groups

    class Meta(UserCreationForm.Meta):
        fields = UserCreationForm.Meta.fields + ('username', 'password1', 'password2', 'first_name', 'last_name', 'email', 'group')