# Generated by Django 3.1.3 on 2020-11-21 03:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0002_auto_20201120_2154'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notificaciones',
            name='notificacion',
            field=models.CharField(blank=True, max_length=400, null=True),
        ),
    ]
