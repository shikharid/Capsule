# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0002_userscore'),
    ]

    operations = [
        migrations.AddField(
            model_name='userscore',
            name='created_on',
            field=models.DateField(default=datetime.datetime(2016, 4, 17, 15, 41, 2, 40665), auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='userscore',
            name='updated_on',
            field=models.DateField(default=datetime.datetime(2016, 4, 17, 15, 41, 10, 183155), auto_now=True),
            preserve_default=False,
        ),
    ]
