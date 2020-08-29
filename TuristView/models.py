from django.db import models

# Create your models here.
from django.utils import timezone


class Locales(models.Model):
    idLocal = models.PositiveIntegerField()
    adminLocal = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    nombreComercial = models.CharField(max_length=200)
    descripcion = models.TextField()
    srcLogo =  models.URLField()
    likes = models.PositiveIntegerField()
    estrellas = models.PositiveIntegerField()
    vistas = models.PositiveIntegerField()
    direccion= models.CharField(max_length=200)
    categoria = models.ForeignKey('Categoria', on_delete=models.CASCADE)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

class Categoria(models.Model):
    idCategoria = models.PositiveIntegerField()
    tipo = models.CharField(max_length=200)
    descripcion = models.TextField()

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title