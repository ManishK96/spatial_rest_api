# Generated by Django 4.0.7 on 2022-09-30 03:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('worldviewer', '0004_spatialdata_task'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='spatialdata',
            name='task',
        ),
        migrations.AlterModelTable(
            name='spatialdata',
            table='worldviewdb',
        ),
    ]
