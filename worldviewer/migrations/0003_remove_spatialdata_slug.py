# Generated by Django 4.1.1 on 2022-09-27 02:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('worldviewer', '0002_spatialdata_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='spatialdata',
            name='slug',
        ),
    ]
