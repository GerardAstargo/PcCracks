# Generated by Django 4.2.1 on 2023-05-23 04:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('rut_cliente', models.CharField(max_length=15, primary_key=True, serialize=False)),
                ('nombre_cliente', models.CharField(max_length=15)),
                ('fecha_nacimiento', models.DateField()),
                ('direccion_cliente', models.CharField(max_length=30)),
                ('email_cliente', models.CharField(max_length=20)),
                ('num_telefonico_cliente', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Compra',
            fields=[
                ('compra_id', models.IntegerField(primary_key=True, serialize=False)),
                ('metodo_pago', models.CharField(max_length=20)),
                ('cantidad_productos', models.IntegerField()),
                ('total_compra', models.IntegerField()),
                ('fecha_compra', models.DateField()),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pcracks.cliente')),
            ],
        ),
        migrations.CreateModel(
            name='Contacto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('correo', models.CharField(max_length=20)),
                ('nombre', models.CharField(max_length=20)),
                ('mensaje', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='Empleado',
            fields=[
                ('rut_empleado', models.CharField(max_length=15, primary_key=True, serialize=False)),
                ('nombre_empleado', models.CharField(max_length=15)),
                ('fecha_nacimiento', models.DateField()),
                ('direccion_empleado', models.CharField(max_length=30)),
                ('email_empleado', models.CharField(max_length=20)),
                ('num_telefonico_empleado', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Foto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('foto', models.ImageField(upload_to='producto')),
            ],
        ),
        migrations.CreateModel(
            name='Pedido',
            fields=[
                ('cod_pedido', models.IntegerField(primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('correo_electronico', models.CharField(max_length=20)),
                ('contrasena', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('marca', models.CharField(max_length=20)),
                ('modelo', models.CharField(max_length=20)),
                ('precio', models.IntegerField()),
                ('compra', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pcracks.compra')),
            ],
        ),
    ]
