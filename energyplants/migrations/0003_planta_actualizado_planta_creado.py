# Generated by Django 4.1.5 on 2023-02-19 04:43

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('energyplants', '0002_rename_tipo_tipoplanta'),
    ]

    operations = [
        migrations.AddField(
            model_name='planta',
            name='actualizado',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='planta',
            name='creado',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
