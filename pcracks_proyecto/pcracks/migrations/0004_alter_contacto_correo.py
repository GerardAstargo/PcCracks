# Generated by Django 4.2.1 on 2023-06-19 02:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pcracks', '0003_rename_contrasena_cliente_cliente_contrasena_cliente'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contacto',
            name='correo',
            field=models.CharField(max_length=50),
        ),
    ]
