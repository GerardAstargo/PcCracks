# Generated by Django 4.2.1 on 2023-05-29 04:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pcracks', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cliente',
            old_name='contrasenaCliente',
            new_name='contrasena_Cliente',
        ),
    ]
