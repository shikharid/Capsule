# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('judge', '0002_submission_error_info'),
    ]

    operations = [
        migrations.AddField(
            model_name='submission',
            name='memory_taken',
            field=models.DecimalField(null=True, max_digits=6, decimal_places=2, blank=True),
        ),
        migrations.AddField(
            model_name='submission',
            name='time_taken',
            field=models.DecimalField(null=True, max_digits=3, decimal_places=2, blank=True),
        ),
    ]
