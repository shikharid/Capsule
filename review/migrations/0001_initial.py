# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('problems', '0004_auto_20160417_1541'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='PlagiarismRequest',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('status', models.BooleanField(default=False)),
                ('created_on', models.DateField(auto_now=True)),
                ('updated_on', models.DateField(auto_now_add=True)),
                ('assignment', models.ForeignKey(to='problems.Assignment')),
            ],
        ),
        migrations.CreateModel(
            name='PlagiarismScore',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('score', models.FloatField(default=0.0)),
                ('created_on', models.DateField(auto_now=True)),
                ('updated_on', models.DateField(auto_now_add=True)),
                ('problem', models.ForeignKey(to='problems.Problem')),
                ('student_a', models.ForeignKey(related_name='studentA', to=settings.AUTH_USER_MODEL)),
                ('student_b', models.ForeignKey(related_name='studentB', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
