# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('delivery', '0002_auto_20151123_1417'),
    ]

    operations = [
        migrations.AddField(
            model_name='posteditem',
            name='mslug',
            field=models.SlugField(default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='route',
            name='rslug',
            field=models.SlugField(default=''),
            preserve_default=False,
        ),
    ]
