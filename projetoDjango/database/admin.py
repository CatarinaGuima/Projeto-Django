from django.contrib import admin
from database import models
# Register your models here.
admin.site.register(models.Produto)
admin.site.register(models.Cadastro)
admin.site.register(models.Estoque)
admin.site.register(models.Financeiro)
admin.site.register(models.RH)
admin.site.register(models.Login)
