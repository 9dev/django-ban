# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('ban', '0003_auto_20160322_1316'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ban',
            name='creator',
            field=models.ForeignKey(default=None, null=True, blank=True, related_name='ban_creator', to=settings.AUTH_USER_MODEL),
        ),
    ]
