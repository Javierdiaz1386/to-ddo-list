# Generated by Django 4.1 on 2022-09-07 13:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todolistApp', '0004_alter_tareastable_plazoparaterminar'),
    ]

    operations = [
        migrations.AddField(
            model_name='tareastable',
            name='usuario',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='tareastable',
            name='nombreTarea',
            field=models.CharField(max_length=40, verbose_name='Nombre de la Tarea'),
        ),
    ]
