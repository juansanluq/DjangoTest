# Generated by Django 2.1.5 on 2019-01-22 19:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('beers', '0008_auto_20190122_1633'),
    ]

    operations = [
        migrations.CreateModel(
            name='Receta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(blank=True, default=django.utils.timezone.now, verbose_name='Created at')),
                ('last_modified_at', models.DateTimeField(blank=True, default=django.utils.timezone.now, verbose_name='Last modified at')),
                ('name', models.CharField(max_length=50, verbose_name='Nombre')),
                ('tiempo_preparacion', models.IntegerField(default=0, verbose_name='Tiempo de preparación')),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete='Created by', related_name='beers_receta_created', to=settings.AUTH_USER_MODEL)),
                ('last_modified_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='beers_receta_last_modified', to=settings.AUTH_USER_MODEL, verbose_name='Last modified by')),
            ],
            options={
                'verbose_name': 'Receta',
                'verbose_name_plural': 'Recetas',
                'ordering': ['-name'],
            },
        ),
    ]
