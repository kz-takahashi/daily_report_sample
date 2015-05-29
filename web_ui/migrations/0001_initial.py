# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('title', models.CharField(max_length=255, verbose_name='Title')),
                ('content', models.TextField(max_length=4096, verbose_name='Content')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('updated_at', models.DateTimeField(verbose_name='Updated at', auto_now=True)),
                ('author', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
