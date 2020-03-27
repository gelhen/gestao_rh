from django.db import models


class Teste(models.Model):
    titulo = models.CharField(max_length=120)
    descricao = models.TextField()

