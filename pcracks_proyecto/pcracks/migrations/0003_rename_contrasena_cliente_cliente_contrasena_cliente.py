# Generated by Django 4.1.5 on 2023-05-29 14:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pcracks', '0002_rename_contrasenacliente_cliente_contrasena_cliente'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cliente',
            old_name='contrasena_Cliente',
            new_name='contrasena_cliente',
        ),
    ]
