# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainsite', '0004_auto_20150909_0243'),
    ]

    operations = [
        migrations.AlterField(
            model_name='phone',
            name='customer',
            field=models.ForeignKey(blank=True, null=True, related_name='phones', to='mainsite.Customer'),
        ),
        migrations.AlterField(
            model_name='phone',
            name='location',
            field=models.ForeignKey(blank=True, null=True, to='mainsite.Location'),
        ),
    ]
