# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainsite', '0003_auto_20150909_0213'),
    ]

    operations = [
        migrations.AlterField(
            model_name='phone',
            name='location',
            field=models.ForeignKey(null=True, blank=True, to='mainsite.Location', related_name='phones'),
        ),
    ]
