# Generated by Django 2.1.5 on 2019-01-22 15:33

import beers.utils
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('beers', '0007_auto_20190109_2044'),
    ]

    operations = [
        migrations.AlterField(
            model_name='beer',
            name='image',
            field=models.ImageField(blank=True, default='/other/images/warning_placeholder.svg', null=True, upload_to=beers.utils.image_upload_location, verbose_name='Imagen'),
        ),
    ]