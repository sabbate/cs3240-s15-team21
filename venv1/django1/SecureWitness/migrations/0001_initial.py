# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='File',
            fields=[
                ('fileID', models.AutoField(serialize=False, primary_key=True)),
                ('authorID', models.IntegerField()),
                ('ReportID', models.IntegerField()),
                ('content', models.CharField(max_length=1000)),
                ('docfile', models.FileField(upload_to='files/', default=False)),
                ('file_name', models.CharField(max_length=100)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Folder',
            fields=[
                ('folderID', models.AutoField(serialize=False, primary_key=True)),
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
                ('GID', models.AutoField(serialize=False, primary_key=True)),
                ('group_name', models.CharField(max_length=100)),
                ('size', models.IntegerField(default=1)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Report',
            fields=[
                ('RID', models.AutoField(serialize=False, primary_key=True)),
                ('authorID', models.IntegerField()),
                ('create_date', models.DateTimeField(verbose_name='date created')),
                ('last_update_date', models.DateTimeField(verbose_name='date of last modification')),
                ('report_name', models.CharField(max_length=200)),
                ('short_desc', models.CharField(max_length=150, default='DEFAULT VALUE')),
                ('long_desc', models.CharField(max_length=300, default='DEFAULT VALUE')),
                ('location', models.CharField(max_length=300, default='DEFAULT VALUE')),
                ('incident_date', models.CharField(max_length=300, default='DEFAULT VALUE')),
                ('keywords', models.CharField(max_length=300, default='DEFAULT VALUE')),
                ('private', models.BooleanField(default=False)),
                ('folderID', models.ForeignKey(to='SecureWitness.File')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ReportSharingGroup',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('sharing_date', models.DateTimeField(verbose_name=datetime.datetime(2015, 4, 13, 15, 52, 48, 989845))),
                ('GID', models.ForeignKey(to='SecureWitness.Group')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ReportSharingUser',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('sharing_date', models.DateTimeField(verbose_name=datetime.datetime(2015, 4, 13, 15, 52, 48, 989845))),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('UID', models.AutoField(serialize=False, primary_key=True)),
                ('username', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=100)),
                ('reg_date', models.DateTimeField(verbose_name='date of registration')),
                ('admin', models.BooleanField(default=False)),
                ('email', models.EmailField(max_length=75)),
                ('privilege', models.CharField(max_length=100, default='DEFAULT VALUE')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='UserToGroup',
            fields=[
                ('ID', models.AutoField(serialize=False, primary_key=True)),
                ('leader', models.BooleanField(default=False)),
                ('request_join', models.BooleanField(default=False)),
                ('GID', models.ForeignKey(to='SecureWitness.Group')),
                ('UID', models.ForeignKey(to='SecureWitness.User')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='reportsharinguser',
            name='UID',
            field=models.ForeignKey(to='SecureWitness.User'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='group',
            name='users',
            field=models.ManyToManyField(through='SecureWitness.UserToGroup', to='SecureWitness.User'),
            preserve_default=True,
        ),
    ]
