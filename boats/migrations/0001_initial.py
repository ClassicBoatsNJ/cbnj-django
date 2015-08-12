# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Boat',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('url_name', models.CharField(max_length=255)),
                ('nice_name', models.CharField(max_length=255)),
                ('subtitle', models.CharField(max_length=255)),
                ('post_text', models.CharField(max_length=255)),
                ('main_image', models.ImageField(upload_to=b'images')),
            ],
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('ordering', models.IntegerField()),
                ('image_file', models.ImageField(upload_to=b'images')),
                ('boat', models.ForeignKey(to='boats.Boat')),
            ],
        ),
    ]
