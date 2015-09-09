# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainsite', '0002_auto_20150829_0318'),
    ]

    operations = [
        migrations.AlterField(
            model_name='phone',
            name='ext',
            field=models.CharField(blank=True, null=True, max_length=25),
        ),
    ]
