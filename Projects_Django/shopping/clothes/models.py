from django.db import models

class Marca(models.Model) :
    nombre = models.CharField(max_length=100)
    pais = models.CharField(max_length=100)
    tipo = models.CharField(max_length=100)

class Sucursal(models.Model) :
    ciudad = models.CharField(max_length=100)
