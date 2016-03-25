# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('problems', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='problem',
            name='time_limit',
            field=models.DecimalField(default=2.0, max_digits=3, decimal_places=1, validators=[django.core.validators.MinValueValidator(1.0)]),
            preserve_default=False,
        ),
    ]
