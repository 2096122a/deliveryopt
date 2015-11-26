# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('delivery', '0005_auto_20151123_1904'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('driver', models.BooleanField(default=False)),
                ('VehicleHeight', models.IntegerField(default=0)),
                ('VehicleLength', models.IntegerField(default=0)),
                ('VehicleWidth', models.IntegerField(default=0)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='posteditem',
            name='dropOffAddress2',
        ),
        migrations.RemoveField(
            model_name='posteditem',
            name='dropOffAddress3',
        ),
        migrations.RemoveField(
            model_name='posteditem',
            name='dropOffAddress4',
        ),
        migrations.RemoveField(
            model_name='posteditem',
            name='pickUpAddress2',
        ),
        migrations.RemoveField(
            model_name='posteditem',
            name='pickUpAddress3',
        ),
        migrations.RemoveField(
            model_name='posteditem',
            name='pickUpAddress4',
        ),
        migrations.AddField(
            model_name='posteditem',
            name='complete',
            field=models.CharField(default=b'pending', max_length=20),
            preserve_default=True,
        ),
    ]
