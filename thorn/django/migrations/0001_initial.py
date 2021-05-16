# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-27 19:33
from __future__ import absolute_import, unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import thorn.generic.models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Subscriber',
            fields=[
                ('id', models.AutoField(
                    auto_created=True, primary_key=True,
                    serialize=False, verbose_name='ID')),
                ('uuid', models.UUIDField(
                    default=uuid.uuid4, editable=False,
                    help_text='Unique identifier for this subscriber.',
                    unique=True, verbose_name='UUID')),
                ('event', models.CharField(choices=[],
                    db_index=True, help_text='Name of event to connect with',
                    max_length=190, verbose_name='event')),
                ('url', models.URLField(
                    db_index=True, help_text='Callback URL',
                    max_length=190, verbose_name='URL')),
                ('content_type', models.CharField(
                    choices=[('application/json', 'application/json'),
                             ('application/x-www-form-urlencoded',
                              'application/x-www-form-urlencoded')],
                    default='application/json',
                    help_text='''
                        Desired content type for requests to this callback.
                    '''.strip(),
                    max_length=190, verbose_name='content type')),
                ('created_at', models.DateTimeField(
                    auto_now_add=True, verbose_name='created at')),
                ('updated_at', models.DateTimeField(
                    auto_now=True, verbose_name='updated_at')),
                ('user', models.ForeignKey(
                    null=True, on_delete=django.db.models.deletion.CASCADE,
                    related_name='webhooks_subscriber',
                    to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['url', '-created_at'],
                'get_latest_by': 'updated_at',
                'verbose_name': 'subscriber',
                'verbose_name_plural': 'subscriber',
            },
            bases=(models.Model, thorn.generic.models.SubscriberModelMixin),
        ),
        migrations.AlterUniqueTogether(
            name='subscriber',
            unique_together=set([('url', 'event')]),
        ),
    ]
