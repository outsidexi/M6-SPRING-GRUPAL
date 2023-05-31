"""
URL configuration for primer_proyecto project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from primera_aplicacion.views import index_welcome, UsersApp, contenido, contenido_proveedores,FormUsers, FormSuppliers, user_login, RestringidaView, register, BienvenidaView
from django.contrib.auth.decorators import login_required
from django.contrib.auth import views 
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index_welcome, name="index"),
    path("users/", login_required(UsersApp.as_view()), name="users"),
    path('clientes/', login_required(contenido), name="clients"),
    path('formulario_usuarios/<int:id>', login_required(FormUsers.as_view()), name='form_users'),
    path('proveedores/',login_required(contenido_proveedores), name="suppliers"),
    path('formulario_proveedores/<int:id>', login_required(FormSuppliers.as_view()), name='form_suppliers'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('restringida/', login_required(RestringidaView.as_view()), name='restringida'),
    path('registro/', register, name='register'),
    path('bienvenida/', BienvenidaView.as_view(), name='bienvenida')
]
