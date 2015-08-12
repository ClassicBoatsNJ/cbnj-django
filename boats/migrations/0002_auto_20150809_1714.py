# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('boats', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='boat',
            name='nice_name',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='boat',
            name='post_text',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='boat',
            name='subtitle',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='boat',
            name='url_name',
            field=models.TextField(),
        ),
    ]
