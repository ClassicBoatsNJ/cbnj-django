# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('boats', '0002_auto_20150809_1714'),
    ]

    operations = [
        migrations.AlterField(
            model_name='boat',
            name='nice_name',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='boat',
            name='subtitle',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='boat',
            name='url_name',
            field=models.CharField(max_length=255),
        ),
    ]
