# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ActivationProfile',
            fields=[
                ('activation_key', models.CharField(default='DEFAULT VALUE', max_length=300)),
                ('user', models.OneToOneField(primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('key_expires', models.DateTimeField(default=datetime.datetime(2015, 4, 26, 21, 21, 32, 272677))),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='File',
            fields=[
                ('file_id', models.AutoField(primary_key=True, serialize=False)),
                ('docfile', models.FileField(upload_to='files/', default=False)),
                ('file_name', models.CharField(max_length=100)),
                ('author', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Folder',
            fields=[
                ('folder_id', models.AutoField(primary_key=True, serialize=False)),
                ('folder_name', models.CharField(max_length=100)),
                ('GID', models.ForeignKey(to='auth.Group')),
                ('author_id', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
                ('parent', models.ForeignKey(null=True, to='SecureWitness.Folder', blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='GroupProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('datetime', models.DateTimeField(verbose_name='date created')),
                ('group', models.OneToOneField(to='auth.Group')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Report',
            fields=[
                ('report_id', models.AutoField(primary_key=True, serialize=False)),
                ('create_date', models.DateTimeField(verbose_name='date created', default=datetime.datetime(2015, 4, 26, 21, 21, 32, 272678))),
                ('last_update_date', models.DateTimeField(verbose_name='date of last modification', default=datetime.datetime(2015, 4, 26, 21, 21, 32, 272678))),
                ('report_name', models.CharField(max_length=200)),
                ('short_desc', models.CharField(default='DEFAULT VALUE', max_length=150)),
                ('long_desc', models.CharField(default='DEFAULT VALUE', max_length=300)),
                ('location', models.CharField(default='DEFAULT VALUE', max_length=300)),
                ('incident_date', models.CharField(default='DEFAULT VALUE', max_length=300)),
                ('keywords', models.CharField(default='DEFAULT VALUE', max_length=300)),
                ('private', models.BooleanField(default=False)),
                ('author_id', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
                ('folder_id', models.ForeignKey(null=True, to='SecureWitness.Folder', blank=True)),
                ('group_id', models.ForeignKey(null=True, to='auth.Group', blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='UserToGroup',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('leader', models.BooleanField(default=False)),
                ('group_id', models.ForeignKey(to='auth.Group')),
                ('user_id', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='file',
            name='report',
            field=models.ForeignKey(to='SecureWitness.Report'),
            preserve_default=True,
        ),
    ]
