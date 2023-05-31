from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission

class CustomUser(AbstractUser):
    groups = models.ManyToManyField(Group, related_name='customuser_set')
    user_permissions = models.ManyToManyField(Permission, related_name='customuser_set')

    pass

class Contenido(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.TextField()
    phone = models.TextField()
    last_name = models.TextField()
    age = models.IntegerField()
    email = models.TextField()

class DatosCliente(models.Model):
    id = models.IntegerField(primary_key=True)
    direccion = models.TextField()
    edad = models.IntegerField()
    profesion = models.TextField()
    
class ContenidoProveedor(models.Model):
    id = models.IntegerField(primary_key=True)
    supplier_name = models.TextField()
    phone = models.TextField()
    email = models.TextField()
    
class DatosProveedor(models.Model):
    id = models.IntegerField(primary_key=True)
    direccion = models.TextField()
    area = models.TextField()
    producto = models.TextField()
    
    class Meta:
        permissions = (
            ("permiso_edicion", "permiso para editar card"),
        )



