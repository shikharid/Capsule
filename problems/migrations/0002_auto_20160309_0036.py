# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
import problems.models


class Migration(migrations.Migration):

    dependencies = [
        ('problems', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='testcase',
            name='created_on',
            field=models.DateField(default=datetime.datetime(2016, 3, 9, 0, 36, 47, 556736), auto_now=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='testcase',
            name='is_used',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='testcase',
            name='updated_on',
            field=models.DateField(default=datetime.datetime(2016, 3, 9, 0, 36, 52, 251702), auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='problem',
            name='statement',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='testcase',
            name='input',
            field=models.FileField(upload_to=problems.models.get_input_file_path),
        ),
        migrations.AlterField(
            model_name='testcase',
            name='output',
            field=models.FileField(upload_to=problems.models.get_output_file_path),
        ),
    ]
