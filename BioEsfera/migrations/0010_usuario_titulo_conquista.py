# Generated by Django 5.1.3 on 2024-11-21 12:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BioEsfera', '0009_remove_conquista_usuario'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='titulo_conquista',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
    ]
