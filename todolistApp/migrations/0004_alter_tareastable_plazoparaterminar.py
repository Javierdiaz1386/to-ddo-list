# Generated by Django 4.1 on 2022-09-06 00:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todolistApp', '0003_alter_tareastable_nombretarea_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tareastable',
            name='plazoParaTerminar',
            field=models.DateField(verbose_name='Plazo Para terminar AAAA-MM-DD'),
        ),
    ]
