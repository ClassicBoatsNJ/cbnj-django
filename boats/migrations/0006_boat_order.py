# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import boats.models


class Migration(migrations.Migration):

    dependencies = [
        ('boats', '0005_auto_20150810_1648'),
    ]

    operations = [
        migrations.AddField(
            model_name='boat',
            name='order',
            field=models.IntegerField(default=boats.models.default_order),
        ),
    ]
