from django.db import models
from django.utils import timezone


class Categoria(models.Model):
    nome = models.CharField(max_length=255)


class Dado(models.Model):
    nome = models.CharField(max_length=255)
    sobrenome = models.CharField(max_length=255)
    telefone = models.CharField(max_length=255, blank=True)
    email = models.CharField(max_length=255, blank=True)
    data_criacao = models.DateTimeField(default=timezone.now)
    numero = models.IntegerField()
    serie = models.CharField(max_length=100)
    data_nascimento = models.DateField(blank=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.DO_NOTHING)


