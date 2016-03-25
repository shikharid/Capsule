# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('problems', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Submission',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('spoj_id', models.CharField(max_length=30, null=True, blank=True)),
                ('code', models.TextField()),
                ('language', models.IntegerField(default=1)),
                ('verdict', models.IntegerField(default=0)),
                ('created_on', models.DateField(auto_now=True)),
                ('updated_on', models.DateField(auto_now_add=True)),
                ('problem_id', models.ForeignKey(to='problems.Problem')),
                ('user_id', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
