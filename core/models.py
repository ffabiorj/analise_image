from random import randint
from django.db import models


def upload_image(filename):
    return f"{randint(1, 1000000)}-{filename}"


STATUS = [("A", "Analisado"), ("N", "Não analisado")]

class Image(models.Model):
    name = models.CharField("nome", max_length=150)
    image =  models.ImageField(upload_to=upload_image, blank=True, null=True)

    def __repr__(self) -> str:
        return self.name

class Analise(models.Model):
    name = models.CharField("nome", max_length=255)
    image = models.ForeignKey(Image, on_delete=models.CASCADE)
    type = models.CharField("tipo", max_length=150)
    created_at = models.DateField("Criado", auto_created=True)
    updated_at = models.DateField("Atualizado", auto_now=True)
    status = models.CharField("status", max_length=15, choices=STATUS)

    def __repr__(self) -> str:
        return self.name
