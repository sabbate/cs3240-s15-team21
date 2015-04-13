# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Files',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('fileID', models.IntegerField()),
                ('authorID', models.IntegerField()),
                ('ReportID', models.IntegerField()),
                ('content', models.CharField(max_length=1000)),
                ('file_name', models.CharField(max_length=100)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Folders',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('folderID', models.IntegerField()),
                ('authorID', models.IntegerField()),
                ('folder_name', models.CharField(max_length=100)),
                ('parent', models.IntegerField()),
                ('GID', models.IntegerField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('GID', models.IntegerField()),
                ('group_name', models.CharField(max_length=100)),
                ('size', models.IntegerField(default=1)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Reports',
            fields=[
                ('RID', models.AutoField(primary_key=True, serialize=False)),
                ('folderID', models.IntegerField(default=0)),
                ('authorID', models.IntegerField(default=0)),
                ('create_date', models.DateTimeField(verbose_name='date created')),
                ('last_update_date', models.DateTimeField(verbose_name='date of last modification')),
                ('short_desc', models.CharField(max_length=150, default='DEFAULT VALUE')),
                ('long_desc', models.CharField(max_length=300, default='DEFAULT VALUE')),
                ('location', models.CharField(max_length=300, default='DEFAULT VALUE')),
                ('incident_date', models.CharField(max_length=300, default='DEFAULT VALUE')),
                ('keywords', models.CharField(max_length=300, default='DEFAULT VALUE')),
                ('private', models.BooleanField(default=False)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('UID', models.IntegerField()),
                ('username', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=100)),
                ('reg_date', models.DateTimeField(verbose_name='date of registration')),
                ('privilege', models.CharField(max_length=100, default='DEFAULT VALUE')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Users_in_groups',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('UID', models.IntegerField()),
                ('GID', models.IntegerField()),
                ('leader', models.BooleanField(default=False)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
