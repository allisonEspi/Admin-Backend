# Generated by Django 3.1.1 on 2020-10-08 20:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0003_auto_20201008_1157'),
    ]

    operations = [
        migrations.AlterField(
            model_name='local',
            name='categoria',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='productos.categoria'),
        ),
    ]
