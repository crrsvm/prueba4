from django.db import models

# Create your models here.


class Servicio(models.Model):
    servicio_id = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

class Proveedor(models.Model):
    rut = models.CharField( max_length=12, primary_key=True)
    nombre = models.CharField(max_length=50)
    descripcion = models.TextField()
    telefono = models.IntegerField()
    email = models.CharField(max_length=50)
    servicio = models.ForeignKey(Servicio, on_delete=models.PROTECT)

    def __str__(self):
        return self.rut

