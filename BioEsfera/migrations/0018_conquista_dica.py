# Generated by Django 5.1.3 on 2024-12-03 00:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BioEsfera', '0017_alter_usuario_avatar_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='conquista',
            name='dica',
            field=models.TextField(default='melhore', max_length=1000),
            preserve_default=False,
        ),
    ]
