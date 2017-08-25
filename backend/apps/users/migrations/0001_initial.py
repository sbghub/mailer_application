# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0006_require_contenttypes_0002'),
    ]

    operations = [
        migrations.CreateModel(
            name='EmailUser',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('password', models.CharField(verbose_name='password', max_length=128)),
                ('last_login', models.DateTimeField(verbose_name='last login', null=True, blank=True)),
                ('is_superuser', models.BooleanField(default=False, verbose_name='superuser status', help_text='Designates that this user has all permissions without explicitly assigning them.')),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('email', models.EmailField(error_messages={'unique': 'That email address is already taken.'}, unique=True, max_length=254)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now)),
                ('last_updated', models.DateTimeField(auto_now=True)),
                ('groups', models.ManyToManyField(verbose_name='groups', help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', blank=True, related_query_name='user', related_name='user_set', to='auth.Group')),
                ('user_permissions', models.ManyToManyField(verbose_name='user permissions', help_text='Specific permissions for this user.', blank=True, related_query_name='user', related_name='user_set', to='auth.Permission')),
            ],
            options={
                'permissions': (('view_emailuser', 'Can view email users'),),
            },
        ),
    ]
