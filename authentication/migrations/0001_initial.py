# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(null=True, verbose_name='last login', blank=True)),
                ('member_id', models.CharField(unique=True, max_length=20, verbose_name=b'College ID')),
                ('email', models.EmailField(unique=True, max_length=255)),
                ('first_name', models.CharField(max_length=30, validators=[django.core.validators.RegexValidator(regex=b'^[a-zA-Z ]+$', message=b'Name should only consist of english alphabets')])),
                ('last_name', models.CharField(max_length=30, validators=[django.core.validators.RegexValidator(regex=b'^[a-zA-Z ]+$', message=b'Name should only consist of english alphabets')])),
                ('is_faculty', models.BooleanField(default=False)),
                ('is_superuser', models.BooleanField(default=False)),
                ('created_on', models.DateField(auto_now_add=True)),
                ('updated_on', models.DateField(auto_now=True)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
