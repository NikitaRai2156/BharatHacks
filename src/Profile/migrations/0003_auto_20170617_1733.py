# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Profile', '0002_auto_20170617_1721'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='postal_code',
            field=models.IntegerField(default=110009),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='profile',
            name='last_name',
            field=models.CharField(default=b'', max_length=50, null=True, blank=True),
        ),
    ]
