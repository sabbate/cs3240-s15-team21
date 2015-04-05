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
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
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
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
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
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
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
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('RID', models.IntegerField()),
                ('folderID', models.IntegerField()),
                ('authorID', models.IntegerField()),
                ('create_date', models.DateTimeField(verbose_name='date created')),
                ('last_update_date', models.DateTimeField(verbose_name='date of last modification')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('UID', models.IntegerField()),
                ('username', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=100)),
                ('reg_date', models.DateTimeField(verbose_name='date of registration')),
                ('privilege', models.CharField(max_length=100)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Users_in_groups',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('UID', models.IntegerField()),
                ('GID', models.IntegerField()),
                ('leader', models.BooleanField(default=False)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
