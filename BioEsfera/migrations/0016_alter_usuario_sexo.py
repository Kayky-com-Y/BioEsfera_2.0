# Generated by Django 5.1.3 on 2024-11-26 13:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BioEsfera', '0015_usuario_descricao_conquista'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='sexo',
            field=models.CharField(blank=True, max_length=150),
        ),
    ]
