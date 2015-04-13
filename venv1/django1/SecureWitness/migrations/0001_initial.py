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
<<<<<<< HEAD
                ('fileID', models.AutoField(serialize=False, primary_key=True)),
=======
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('fileID', models.IntegerField()),
>>>>>>> development
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
<<<<<<< HEAD
                ('folderID', models.AutoField(serialize=False, primary_key=True)),
=======
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('folderID', models.IntegerField()),
>>>>>>> development
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
<<<<<<< HEAD
                ('GID', models.AutoField(serialize=False, primary_key=True)),
=======
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('GID', models.IntegerField()),
>>>>>>> development
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
<<<<<<< HEAD
                ('RID', models.AutoField(serialize=False, primary_key=True)),
                ('authorID', models.IntegerField()),
                ('create_date', models.DateTimeField(verbose_name='date created')),
                ('last_update_date', models.DateTimeField(verbose_name='date of last modification')),
                ('report_name', models.CharField(max_length=200)),
                ('folderID', models.ForeignKey(to='SecureWitness.File')),
=======
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
>>>>>>> development
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='User',
            fields=[
<<<<<<< HEAD
                ('UID', models.AutoField(serialize=False, primary_key=True)),
                ('username', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=100)),
                ('reg_date', models.DateTimeField(verbose_name='date of registration')),
                ('admin', models.BooleanField(default=False)),
=======
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('UID', models.IntegerField()),
                ('username', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=100)),
                ('reg_date', models.DateTimeField(verbose_name='date of registration')),
                ('privilege', models.CharField(max_length=100, default='DEFAULT VALUE')),
>>>>>>> development
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='UserToGroup',
            fields=[
<<<<<<< HEAD
                ('ID', models.AutoField(serialize=False, primary_key=True)),
=======
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('UID', models.IntegerField()),
                ('GID', models.IntegerField()),
>>>>>>> development
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
