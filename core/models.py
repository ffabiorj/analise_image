from random import randint
from django.db import models


STATUS = [("A", "Analisado"), ("N", "Não analisado")]


def upload_image(instance, filename):
    return f"{randint(1, 1000000)}-{filename}"


class Imagem(models.Model):
    nome = models.CharField("nome", max_length=150)
    imagem = models.ImageField(upload_to=upload_image)

    def __repr__(self):
        return self.nome

    def __str__(self):
        return self.nome


class Analise(models.Model):
    nome = models.CharField(max_length=255)
    imagem = models.ForeignKey(
        Imagem, on_delete=models.CASCADE,
        related_name="analises"
    )
    tipo = models.CharField(max_length=150)
    criado_em = models.DateField(auto_now_add=True)
    atualizado_em = models.DateField(auto_now=True)
    status = models.CharField(max_length=15, choices=STATUS)

    def __repr__(self):
        return self.nome

    def __str__(self):
        return self.nome
