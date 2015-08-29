# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainsite', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='customer',
            field=models.ForeignKey(to='mainsite.Customer', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='address',
            name='location',
            field=models.ForeignKey(to='mainsite.Location', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='address',
            name='session',
            field=models.ForeignKey(to='mainsite.Session', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='email',
            name='customer',
            field=models.ForeignKey(to='mainsite.Customer', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='email',
            name='location',
            field=models.ForeignKey(to='mainsite.Location', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='link',
            name='customer',
            field=models.ForeignKey(to='mainsite.Customer', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='link',
            name='location',
            field=models.ForeignKey(to='mainsite.Location', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='link',
            name='session',
            field=models.ForeignKey(to='mainsite.Session', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='phone',
            name='customer',
            field=models.ForeignKey(to='mainsite.Customer', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='phone',
            name='location',
            field=models.ForeignKey(to='mainsite.Location', null=True, blank=True),
        ),
    ]
