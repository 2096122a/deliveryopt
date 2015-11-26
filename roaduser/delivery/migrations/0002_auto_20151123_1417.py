# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('delivery', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='posteditem',
            name='destination',
        ),
        migrations.RemoveField(
            model_name='posteditem',
            name='name',
        ),
        migrations.RemoveField(
            model_name='route',
            name='views',
        ),
        migrations.AddField(
            model_name='posteditem',
            name='RecipientName',
            field=models.CharField(default=b'', max_length=128),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='posteditem',
            name='SenderName',
            field=models.CharField(default=b'', max_length=128),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='posteditem',
            name='dropOffAddress1',
            field=models.CharField(default=b'', max_length=128),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='posteditem',
            name='dropOffAddress2',
            field=models.CharField(default=b'', max_length=128),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='posteditem',
            name='dropOffAddress3',
            field=models.CharField(default=b'', max_length=128, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='posteditem',
            name='dropOffAddress4',
            field=models.CharField(default=b'', max_length=128, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='posteditem',
            name='dropOffContactNumber',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='posteditem',
            name='dropOffPostCode',
            field=models.CharField(default=b'', max_length=128),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='posteditem',
            name='itemName',
            field=models.CharField(default=b'', max_length=128),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='posteditem',
            name='pickUpAddress1',
            field=models.CharField(default=b'', max_length=128),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='posteditem',
            name='pickUpAddress2',
            field=models.CharField(default=b'', max_length=128),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='posteditem',
            name='pickUpAddress3',
            field=models.CharField(default=b'', max_length=128, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='posteditem',
            name='pickUpAddress4',
            field=models.CharField(default=b'', max_length=128, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='posteditem',
            name='pickUpContactNumber',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='posteditem',
            name='pickUpPostCode',
            field=models.CharField(default=b'', max_length=128),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='route',
            name='driverName',
            field=models.CharField(default=b'', max_length=128),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='route',
            name='end',
            field=models.CharField(default=b'', max_length=128),
        ),
        migrations.AlterField(
            model_name='route',
            name='start',
            field=models.CharField(default=b'', max_length=128),
        ),
        migrations.AlterField(
            model_name='route',
            name='via',
            field=models.CharField(default=b'', max_length=128, null=True),
        ),
    ]
