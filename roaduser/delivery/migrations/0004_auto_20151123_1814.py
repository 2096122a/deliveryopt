# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('delivery', '0003_auto_20151123_1749'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posteditem',
            name='mslug',
            field=models.SlugField(unique=True),
        ),
        migrations.AlterField(
            model_name='route',
            name='rslug',
            field=models.SlugField(unique=True),
        ),
    ]
