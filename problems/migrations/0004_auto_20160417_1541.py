# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('problems', '0003_auto_20160417_0102'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='assignmentscore',
            unique_together=set([('student', 'assignment')]),
        ),
        migrations.AlterUniqueTogether(
            name='problemscore',
            unique_together=set([('student', 'problem')]),
        ),
    ]
