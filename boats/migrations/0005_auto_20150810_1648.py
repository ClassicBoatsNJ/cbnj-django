# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('boats', '0004_auto_20150809_2044'),
    ]

    operations = [
        migrations.AlterField(
            model_name='boat',
            name='main_image',
            field=models.ImageField(upload_to=b''),
        ),
        migrations.AlterField(
            model_name='image',
            name='image_file',
            field=models.ImageField(upload_to=b''),
        ),
    ]
