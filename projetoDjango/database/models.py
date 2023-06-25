from django.db import models

# Create your models here.
#Módulo Login
class Login(models.Model):
    username = models.EmailField(max_length=60, unique=True) 
    password = models.CharField(max_length=128)

    def __str__(self):
        return self.username

#Módulo Cadastro
class Cadastro(models.Model):
    
    opcoes_funcoes = (
        ('gerente', 'Gerente'),
        ('caixa', 'Caixa'),
        ('estoquista', 'Estoquista'),
        ('administrativo', 'Administrativo'),
    )

    nome = models.CharField(max_length=100)
    opcoes_funcoes = models.CharField(max_length=50, choices=opcoes_funcoes)
    email = models.EmailField(unique=True)
    telefone = models.CharField(max_length=20)

    def __str__(self):
        return self.nome

#Módulo Produto
class Produto(models.Model):
    identificador = models.AutoField(primary_key=True)
    quantidade_estoque = models.PositiveIntegerField()
    descricao = models.TextField()
    nome = models.CharField(max_length=100)
    preco = models.DecimalField(max_digits=8, decimal_places=2)
    categoria = models.CharField(max_length=100, default='Sem Categoria')
    tipo = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

#Módulo Estoque
class Estoque(models.Model):
    setor = models.CharField(max_length=100)
    corredor = models.IntegerField(default=0)
    prateleira = models.IntegerField(default=0)
    nome_produto = models.CharField(max_length=100)

    def __str__(self):
        return self.setor
    
#Módulo Financeiro
class Financeiro(models.Model):
    opcoes_tipo = (
        ('Compra', 'Compra'),
        ('Venda', 'Venda'),
    )

    opcoes_status = (
        ('Pendente', 'Pendente'),
        ('Concluído', 'Concluído'),
        ('Cancelado', 'Cancelado'),
    )

    tipo = models.CharField(max_length=10, choices=opcoes_tipo, default='Sem Tipo')
    status = models.CharField(max_length=10, choices=opcoes_status)
    data = models.DateTimeField(auto_now_add=True)
    descricao = models.TextField()
    valor = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        verbose_name_plural = 'Financeiro'

    def __str__(self):
        return f'{self.tipo} - {self.data}'

# Módulo Recursos Humanos
class RecursosHumano(models.Model):
    funcionario = models.CharField(max_length=100)
    cargo = models.CharField(max_length=100)
    salario = models.DecimalField(max_digits=8, decimal_places=2)
    carga_horaria = models.IntegerField()
    folha_de_ponto = models.CharField(max_length=100)
    setor = models.CharField(max_length=100)    

    def __str__(self):
        return self.funcionario