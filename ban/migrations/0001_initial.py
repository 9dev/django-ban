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
            name='Ban',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('end_date', models.DateTimeField(null=True, default=None)),
                ('creator', models.ForeignKey(to=settings.AUTH_USER_MODEL, related_name='creator')),
                ('receiver', models.ForeignKey(unique=True, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
