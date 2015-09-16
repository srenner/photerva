# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('mainsite', '0005_auto_20150909_0246'),
    ]

    operations = [
        migrations.CreateModel(
            name='EmailAddress',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('email_address', models.CharField(max_length=200)),
            ],
        ),
        migrations.RemoveField(
            model_name='email',
            name='customer',
        ),
        migrations.RemoveField(
            model_name='email',
            name='location',
        ),
        migrations.RenameField(
            model_name='customer',
            old_name='user',
            new_name='owner',
        ),
        migrations.RenameField(
            model_name='location',
            old_name='user',
            new_name='owner',
        ),
        migrations.RenameField(
            model_name='session',
            old_name='user',
            new_name='owner',
        ),
        migrations.RenameField(
            model_name='sessiontype',
            old_name='user',
            new_name='owner',
        ),
        migrations.AddField(
            model_name='address',
            name='owner',
            field=models.ForeignKey(default=1, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='link',
            name='owner',
            field=models.ForeignKey(default=1, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='phone',
            name='owner',
            field=models.ForeignKey(default=1, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='Email',
        ),
        migrations.AddField(
            model_name='emailaddress',
            name='customer',
            field=models.ForeignKey(to='mainsite.Customer', null=True, blank=True),
        ),
        migrations.AddField(
            model_name='emailaddress',
            name='location',
            field=models.ForeignKey(to='mainsite.Location', null=True, blank=True),
        ),
        migrations.AddField(
            model_name='emailaddress',
            name='owner',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
    ]
