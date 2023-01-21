from django.db import models

# Create your models here.
class Registros(models.Model):
    nome = models.CharField(max_length=40)
    horario = models.TimeField()
    local = models.CharField(max_length=50)
    intensidade = models.CharField(max_length=20)
    clas = models.CharField(max_length=13)