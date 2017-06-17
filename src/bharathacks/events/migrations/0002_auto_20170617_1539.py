# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MasterEventList',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name=b'Created At')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name=b'Updated At')),
                ('name', models.CharField(max_length=255, serialize=False, primary_key=True)),
            ],
            options={
                'db_table': 'event_master_list',
            },
        ),
        migrations.RemoveField(
            model_name='eventtype',
            name='name',
        ),
        migrations.AddField(
            model_name='eventtype',
            name='master_event',
            field=models.ForeignKey(default='', to='events.MasterEventList'),
            preserve_default=False,
        ),
    ]
