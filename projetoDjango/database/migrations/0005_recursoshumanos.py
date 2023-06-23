# Generated by Django 4.2.1 on 2023-06-23 02:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0004_financeiro'),
    ]

    operations = [
        migrations.CreateModel(
            name='RecursosHumanos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('funcionario', models.CharField(max_length=100)),
                ('cargo', models.CharField(max_length=100)),
                ('salario', models.DecimalField(decimal_places=2, max_digits=8)),
                ('carga_horaria', models.IntegerField()),
                ('folha_de_ponto', models.CharField(max_length=100)),
                ('setor', models.CharField(max_length=100)),
            ],
        ),
    ]
