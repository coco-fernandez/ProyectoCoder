# Generated by Django 4.0.5 on 2022-07-18 02:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ProyectoCoderApp', '0004_entregable'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bandas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('genero', models.CharField(max_length=30)),
                ('cantidad_integrantes', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Estudios',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('ubicacion', models.CharField(max_length=30)),
                ('cantidad_salas', models.IntegerField()),
            ],
        ),
        migrations.RenameModel(
            old_name='Estudiante',
            new_name='Productores',
        ),
        migrations.DeleteModel(
            name='Curso',
        ),
        migrations.DeleteModel(
            name='Entregable',
        ),
        migrations.DeleteModel(
            name='Profesor',
        ),
        migrations.AlterModelOptions(
            name='productores',
            options={'verbose_name_plural': 'Productores'},
        ),
    ]