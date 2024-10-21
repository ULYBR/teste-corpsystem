from django.db import models

class GrupoProduto(models.Model):
    nome = models.CharField(max_length=255)

    def __str__(self):
        return self.nome

class Produto(models.Model):
    nome = models.CharField(max_length=255)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    grupo = models.ForeignKey(GrupoProduto, related_name='produtos', on_delete=models.CASCADE)

    def __str__(self):
        return self.nome
