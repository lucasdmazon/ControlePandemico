from django.db import models
from django.utils import timezone
from cpf_field.models import CPFField


class Categoria(models.Model):
    nome = models.CharField(max_length=255)

    def __str__(self):
        return self.nome


class Dado(models.Model):
    nome = models.CharField(max_length=255)
    sobrenome = models.CharField(max_length=255)
    telefone = models.CharField(max_length=255, blank=True)
    email = models.CharField(max_length=255, blank=True)
    data_criacao = models.DateTimeField(default=timezone.now)
    numero = models.IntegerField()
    serie = models.CharField(max_length=20)
    data_nascimento = models.DateField(blank=True)
    cpf = CPFField('cpf')
    categoria = models.ForeignKey(Categoria, on_delete=models.DO_NOTHING)
    mostrar = models.BooleanField(default=True)

    def __str__(self):
        return self.nome
