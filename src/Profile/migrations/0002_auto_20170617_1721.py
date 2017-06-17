# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('Profile', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='address_1',
            field=models.CharField(default=b'', max_length=200),
        ),
        migrations.AddField(
            model_name='profile',
            name='address_2',
            field=models.CharField(default=b'', max_length=200, blank=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='city',
            field=models.CharField(default=b'', max_length=50),
        ),
        migrations.AddField(
            model_name='profile',
            name='country',
            field=models.CharField(default=b'', max_length=50),
        ),
        migrations.AddField(
            model_name='profile',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2017, 6, 17, 11, 51, 19, 945964, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='profile',
            name='first_name',
            field=models.CharField(default=b'', max_length=50),
        ),
        migrations.AddField(
            model_name='profile',
            name='last_name',
            field=models.CharField(default=b'', max_length=50),
        ),
        migrations.AddField(
            model_name='profile',
            name='mobile',
            field=models.CharField(default=b'', max_length=10),
        ),
        migrations.AddField(
            model_name='profile',
            name='state',
            field=models.CharField(default=b'', max_length=50),
        ),
        migrations.AddField(
            model_name='profile',
            name='updated',
            field=models.DateTimeField(default=datetime.datetime(2017, 6, 17, 11, 51, 29, 44457, tzinfo=utc), auto_now=True),
            preserve_default=False,
        ),
    ]
