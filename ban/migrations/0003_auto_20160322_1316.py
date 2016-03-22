# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('ban', '0002_auto_20160322_0847'),
    ]

    operations = [
        migrations.CreateModel(
            name='Warn',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('creator', models.ForeignKey(to=settings.AUTH_USER_MODEL, related_name='warn_creator')),
                ('receiver', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AlterField(
            model_name='ban',
            name='creator',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, related_name='ban_creator'),
        ),
    ]
