# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


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
                ('folderID', models.ForeignKey(to='SecureWitness.File')),
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
                ('GID', models.ForeignKey(to='SecureWitness.Group')),
                ('UID', models.ForeignKey(to='SecureWitness.User')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='group',
            name='users',
            field=models.ManyToManyField(through='SecureWitness.UserToGroup', to='SecureWitness.User'),
            preserve_default=True,
        ),
    ]
