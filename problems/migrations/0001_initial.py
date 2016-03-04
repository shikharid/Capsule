# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Assignment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('subject_code', models.CharField(max_length=15, null=True, blank=True)),
                ('batch_prefix', models.CharField(max_length=50)),
                ('deadline', models.DateField(null=True, blank=True)),
                ('created_on', models.DateField(auto_now=True)),
                ('updated_on', models.DateField(auto_now_add=True)),
                ('faculty_id', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Problem',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('statement', models.CharField(max_length=2000)),
                ('name', models.CharField(max_length=50)),
                ('points', models.IntegerField(validators=[django.core.validators.MinValueValidator(0)])),
                ('created_on', models.DateField(auto_now=True)),
                ('updated_on', models.DateField(auto_now_add=True)),
                ('assignment_id', models.ForeignKey(to='problems.Assignment')),
            ],
        ),
        migrations.CreateModel(
            name='TestCase',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('input', models.CharField(max_length=1000000)),
                ('output', models.CharField(max_length=1000000)),
                ('problem_id', models.ForeignKey(to='problems.Problem')),
            ],
        ),
    ]
