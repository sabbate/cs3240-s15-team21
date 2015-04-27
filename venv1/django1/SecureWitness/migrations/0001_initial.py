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
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL, serialize=False, primary_key=True)),
                ('key_expires', models.DateTimeField(default=datetime.datetime(2015, 4, 26, 18, 57, 57, 268603))),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='File',
            fields=[
                ('file_id', models.AutoField(serialize=False, primary_key=True)),
                ('docfile', models.FileField(default=False, upload_to='files/')),
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
                ('folder_id', models.AutoField(serialize=False, primary_key=True)),
                ('folder_name', models.CharField(max_length=100)),
                ('GID', models.ForeignKey(to='auth.Group')),
                ('author_id', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
                ('parent', models.ForeignKey(to='SecureWitness.Folder', null=True, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='GroupProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
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
                ('report_id', models.AutoField(serialize=False, primary_key=True)),
                ('create_date', models.DateTimeField(verbose_name='date created')),
                ('last_update_date', models.DateTimeField(verbose_name='date of last modification')),
                ('report_name', models.CharField(max_length=200)),
                ('short_desc', models.CharField(default='DEFAULT VALUE', max_length=150)),
                ('long_desc', models.CharField(default='DEFAULT VALUE', max_length=300)),
                ('location', models.CharField(default='DEFAULT VALUE', max_length=300)),
                ('incident_date', models.CharField(default='DEFAULT VALUE', max_length=300)),
                ('keywords', models.CharField(default='DEFAULT VALUE', max_length=300)),
                ('private', models.BooleanField(default=False)),
                ('author', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
                ('folder', models.ForeignKey(default=0, to='SecureWitness.Folder')),
                ('group', models.ForeignKey(to='auth.Group', null=True, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='UserToGroup',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
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
