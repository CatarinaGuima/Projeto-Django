from django.db import models

# Create your models here.
class Produto(models.Model):
    identificador = models.AutoField(primary_key=True)
    quantidade_estoque = models.PositiveIntegerField()
    descricao = models.TextField()
    nome = models.CharField(max_length=100)
    preco = models.DecimalField(max_digits=8, decimal_places=2)
    categoria = models.CharField(max_length=100, default='Sem Categoria')
    tipo = models.CharField(max_length=100)

    def _str_(self):
        return self.nome
