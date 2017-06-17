# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name=b'Created At')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name=b'Updated At')),
                ('name', models.CharField(max_length=512)),
                ('location', models.TextField(default=b'')),
                ('scheduled_date', models.DateTimeField(null=True, blank=True)),
                ('description', models.TextField(default=b'')),
                ('contact_details', models.TextField(default=b'')),
                ('capacity_count', models.IntegerField(default=0)),
                ('like_count', models.IntegerField(default=0)),
                ('created_by', models.ForeignKey(related_name='created_event_set', verbose_name=b'Created By', blank=True, to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
                'db_table': 'events',
            },
        ),
        migrations.CreateModel(
            name='EventType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name=b'Created At')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name=b'Updated At')),
                ('name', models.CharField(max_length=512)),
                ('subcategory', models.CharField(max_length=512)),
            ],
            options={
                'db_table': 'event_type',
            },
        ),
        migrations.AddField(
            model_name='event',
            name='event_type',
            field=models.ForeignKey(to='events.EventType'),
        ),
        migrations.AddField(
            model_name='event',
            name='updated_by',
            field=models.ForeignKey(related_name='updated_event_set', verbose_name=b'Updated By', blank=True, to=settings.AUTH_USER_MODEL, null=True),
        ),
    ]
