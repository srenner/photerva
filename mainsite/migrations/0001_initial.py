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
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('address1', models.CharField(max_length=100)),
                ('address2', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=100)),
                ('state', models.CharField(max_length=100)),
                ('zip', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('notes', models.TextField()),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Email',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=200)),
                ('customer', models.ForeignKey(to='mainsite.Customer')),
            ],
        ),
        migrations.CreateModel(
            name='Link',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('url', models.URLField()),
                ('customer', models.ForeignKey(to='mainsite.Customer')),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('notes', models.TextField()),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Phone',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=25)),
                ('ext', models.CharField(max_length=25)),
                ('customer', models.ForeignKey(to='mainsite.Customer')),
                ('location', models.ForeignKey(to='mainsite.Location')),
            ],
        ),
        migrations.CreateModel(
            name='Session',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('datetime', models.DateTimeField()),
                ('backup_datetime', models.DateTimeField()),
                ('notes', models.TextField()),
                ('quoted_price', models.DecimalField(decimal_places=2, max_digits=8)),
                ('final_price', models.DecimalField(decimal_places=2, max_digits=8)),
                ('expenses', models.DecimalField(decimal_places=2, max_digits=8)),
                ('shoot_time', models.TimeField()),
                ('edit_time', models.TimeField()),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='SessionType',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('notes', models.TextField()),
                ('base_price', models.DecimalField(decimal_places=2, max_digits=8)),
                ('shoot_time', models.TimeField()),
                ('edit_time', models.TimeField()),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='link',
            name='location',
            field=models.ForeignKey(to='mainsite.Location'),
        ),
        migrations.AddField(
            model_name='link',
            name='session',
            field=models.ForeignKey(to='mainsite.Session'),
        ),
        migrations.AddField(
            model_name='email',
            name='location',
            field=models.ForeignKey(to='mainsite.Location'),
        ),
        migrations.AddField(
            model_name='address',
            name='customer',
            field=models.ForeignKey(to='mainsite.Customer'),
        ),
        migrations.AddField(
            model_name='address',
            name='location',
            field=models.ForeignKey(to='mainsite.Location'),
        ),
        migrations.AddField(
            model_name='address',
            name='session',
            field=models.ForeignKey(to='mainsite.Session'),
        ),
    ]
