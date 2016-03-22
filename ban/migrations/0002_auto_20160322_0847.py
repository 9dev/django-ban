# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ban', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ban',
            name='end_date',
            field=models.DateTimeField(blank=True, null=True, default=None),
        ),
    ]
