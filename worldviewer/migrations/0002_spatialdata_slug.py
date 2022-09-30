# Generated by Django 4.1.1 on 2022-09-27 01:31

from django.db import migrations
import django_extensions.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('worldviewer', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='spatialdata',
            name='slug',
            field=django_extensions.db.fields.AutoSlugField(blank=True, editable=False, help_text='A label for URL config.', max_length=31, populate_from='ADMIN'),
        ),
    ]
