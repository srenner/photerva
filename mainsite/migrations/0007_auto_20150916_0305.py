# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainsite', '0006_auto_20150916_0219'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='location',
            name='owner',
        ),
        migrations.RemoveField(
            model_name='address',
            name='location',
        ),
        migrations.RemoveField(
            model_name='emailaddress',
            name='location',
        ),
        migrations.RemoveField(
            model_name='link',
            name='location',
        ),
        migrations.RemoveField(
            model_name='phone',
            name='location',
        ),
        migrations.RemoveField(
            model_name='phone',
            name='name',
        ),
        migrations.AddField(
            model_name='session',
            name='customer',
            field=models.ForeignKey(default=1, to='mainsite.Customer'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='address',
            name='customer',
            field=models.ForeignKey(blank=True, null=True, to='mainsite.Customer', related_name='addresses'),
        ),
        migrations.AlterField(
            model_name='address',
            name='session',
            field=models.ForeignKey(blank=True, null=True, to='mainsite.Session', related_name='addresses'),
        ),
        migrations.AlterField(
            model_name='session',
            name='backup_datetime',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.DeleteModel(
            name='Location',
        ),
    ]
