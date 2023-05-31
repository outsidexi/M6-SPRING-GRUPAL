from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.http import HttpResponse
from django.contrib.auth.models import User, Group
from django.contrib.auth import authenticate, login, logout
from .models import Contenido, DatosCliente, DatosProveedor, ContenidoProveedor
from primera_aplicacion.forms.formulario import FormularioUsuarioForm, FormularioSupplierForm, LoginForm, RegistrationForm
from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin
from django.contrib.auth.decorators import permission_required
from django.contrib.auth.hashers import make_password


# Create your views here.


def index_welcome(request):
    return render(request, 'welcome.html')


class UsersApp(TemplateView):
    template_name = "users.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['usuarios'] = User.objects.all()

        return context


class FormUsers(TemplateView):
    template_name = 'form_user.html'

    def get_context_data(self, **kwargs):
        contexto = super(FormUsers, self).get_context_data(**kwargs)
        contexto["username"] = self.kwargs["id"]
        contexto["form"] = FormularioUsuarioForm()
        return contexto

    def post(self, request, **kwargs):
        print("entro a post")
        form = FormularioUsuarioForm(request.POST)
        if form.is_valid():
            username = self.kwargs["id"]
            direccion = form.cleaned_data["direccion"]
            edad = form.cleaned_data["edad"]
            profesion = form.cleaned_data["profesion"]
            print("Formulario Valido")
            print(username, direccion, edad, profesion)
            datos = DatosCliente(
                id=username, direccion=direccion, edad=edad, profesion=profesion)
            datos.save()
        else:
            print("Formulario Invalido")
            print(form)
        return redirect('/clientes')


class SupplierApp(PermissionRequiredMixin, LoginRequiredMixin, TemplateView):
    template_name = "suppliers.html"
    print('################## LLEGO #########')
    permission_required = 'primera_aplicacion.permiso_edicion'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['proveedores'] = User.objects.all()

        return context


class FormSuppliers(PermissionRequiredMixin, LoginRequiredMixin, TemplateView):
    template_name = 'form_suppliers.html'
    permission_required = 'primera_aplicacion.permiso_edicion'

    def get_context_data(self, **kwargs):
        contexto = super(FormSuppliers, self).get_context_data(**kwargs)
        contexto["supplier_name"] = self.kwargs["id"]
        contexto["form"] = FormularioSupplierForm()
        return contexto

    def post(self, request, **kwargs):
        print("entro a post")
        form = FormularioSupplierForm(request.POST)
        if form.is_valid():
            supplier_name = self.kwargs["id"]
            direccion = form.cleaned_data["direccion"]
            area = form.cleaned_data["area"]
            producto = form.cleaned_data["producto"]
            print("Formulario Valido")
            print(supplier_name, direccion, area, producto)
            datos = DatosProveedor(
                id=supplier_name, direccion=direccion, area=area, producto=producto)
            datos.save()
        else:
            print("Formulario Invalido")
            print(form)
        return redirect('/proveedores')


class RestringidaView(TemplateView):    
    template_name = 'restringida.html'

class BienvenidaView(TemplateView):    
    template_name = 'bienvenida.html'


def contenido(request):
    datos = Contenido.objects.all()
    print(f'se ha impreso datos de contenido {datos}')
    contexto = {'datos': datos}

    return render(request, 'contenido.html', contexto)

@permission_required('primera_aplicacion.permiso_edicion')
def contenido_proveedores(request):
    datos_proveedor = ContenidoProveedor.objects.all()
    print(f'se ha impreso {datos_proveedor}')
    contexto = {'datos_proveedor': datos_proveedor}

    return render(request, 'contenido_proveedores.html', contexto)

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        
        if form.is_valid():
            username = form.cleaned_data["username"]
            first_name = form.cleaned_data["first_name"]
            last_name = form.cleaned_data["last_name"]
            password = form.cleaned_data['password1']
            email = form.cleaned_data["email"]
            grupo = form.cleaned_data['group']
            
            # Crear el nuevo usuario en la base de datos "default"
            usuario_nuevo = User(username=username, first_name=first_name, last_name=last_name, email=email)
            usuario_nuevo.set_password(password)
            usuario_nuevo.save(using='default')
            
            # Agregar el usuario al grupo en la misma base de datos
            grupo.user_set.add(usuario_nuevo)
            grupo.save(using='default')
            
            # Autenticar y redirigir al usuario
            user = authenticate(request, username=username, password=password)
            login(request, user)
            return redirect('/bienvenida')  # Cambia 'home' por la URL de tu página de inicio
    else:
        form = RegistrationForm(groups=Group.objects.all())  # Pasar los grupos al formulario
    
    return render(request, 'registro.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            print("Formulario Valido")
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            print(username, password)
            user = authenticate(request, username=username, password=password)
            
            if user is not None:
                if user.is_active:
                    print("Usuario activo")
                    login(request, user)
                    return redirect('http://127.0.0.1:8000/')

                else:
                    print("Usuario inactivo")
                    return HttpResponse('Cuenta deshabilitada')
            else:
                print("Usuario o contraseña incorrectos")
                return HttpResponse('Login no Valido')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})
