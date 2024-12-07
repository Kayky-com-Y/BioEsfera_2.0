# Generated by Django 5.1.3 on 2024-11-24 18:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BioEsfera', '0012_alter_usuario_avatar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='avatar',
            field=models.ImageField(blank=True, default='images/cebolo_avatar.png', null=True, upload_to='images/'),
        ),
        migrations.AlterUniqueTogether(
            name='conquista_usuario',
            unique_together={('usuario', 'conquista')},
        ),
    ]
