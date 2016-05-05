# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('judge', '0003_auto_20160310_2346'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='submission',
            name='spoj_id',
        ),
        migrations.AlterField(
            model_name='submission',
            name='language',
            field=models.IntegerField(default=1, choices=[(0, b'C'), (1, b'C++'), (2, b'Java'), (3, b'Python')]),
        ),
        migrations.AlterField(
            model_name='submission',
            name='verdict',
            field=models.IntegerField(default=0, choices=[(0, b'Running'), (1, b'Accepted'), (2, b'Wrong Answer'), (3, b'Compilation Error'), (4, b'Runtime Error'), (5, b'Memory Limit Exceeded'), (6, b'Time Limit Exceeded'), (7, b'Internal Server Error')]),
        ),
    ]
