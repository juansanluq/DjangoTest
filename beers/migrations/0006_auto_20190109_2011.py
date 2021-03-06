# Generated by Django 2.1.5 on 2019-01-09 19:11

import beers.utils
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('beers', '0005_auto_20190106_2321'),
    ]

    operations = [
        migrations.AddField(
            model_name='beer',
            name='descripcion',
            field=models.CharField(default='Introduce una descripción para la cerveza, por defecto mantendrá esta', max_length=250, verbose_name='Descripción'),
        ),
        migrations.AlterField(
            model_name='beer',
            name='image',
            field=models.ImageField(blank=True, default='/static/img/imagen_placeholder.svg', null=True, upload_to=beers.utils.image_upload_location, verbose_name='Imagen'),
        ),
    ]
