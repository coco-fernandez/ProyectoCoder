# Generated by Django 4.0.5 on 2022-07-18 02:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ProyectoCoderApp', '0005_bandas_estudios_rename_estudiante_productores_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='bandas',
            options={'verbose_name_plural': 'Bandas'},
        ),
        migrations.AlterModelOptions(
            name='estudios',
            options={'verbose_name_plural': 'Estudios'},
        ),
    ]
