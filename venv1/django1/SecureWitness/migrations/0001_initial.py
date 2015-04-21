# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='File',
            fields=[
                ('file_id', models.AutoField(primary_key=True, serialize=False)),
                ('docfile', models.FileField(default=False, upload_to='files/')),
                ('file_name', models.CharField(max_length=100)),
                ('author_id', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
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
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Group',
            fields=[
                ('group_id', models.AutoField(primary_key=True, serialize=False)),
                ('group_name', models.CharField(max_length=100)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Report',
            fields=[
                ('report_id', models.AutoField(primary_key=True, serialize=False)),
                ('create_date', models.DateTimeField(verbose_name='date created')),
                ('last_update_date', models.DateTimeField(verbose_name='date of last modification')),
                ('report_name', models.CharField(max_length=200)),
                ('short_desc', models.CharField(default='DEFAULT VALUE', max_length=150)),
                ('long_desc', models.CharField(default='DEFAULT VALUE', max_length=300)),
                ('location', models.CharField(default='DEFAULT VALUE', max_length=300)),
                ('incident_date', models.CharField(default='DEFAULT VALUE', max_length=300)),
                ('keywords', models.CharField(default='DEFAULT VALUE', max_length=300)),
                ('private', models.BooleanField(default=False)),
                ('author_id', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
                ('folder_id', models.ForeignKey(default=0, to='SecureWitness.Folder')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ReportSharingGroup',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('sharing_date', models.DateTimeField()),
                ('group_id', models.ForeignKey(to='SecureWitness.Group')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ReportSharingUser',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('sharing_date', models.DateTimeField()),
                ('user_id', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
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
                ('group_id', models.ForeignKey(to='SecureWitness.Group')),
                ('user_id', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='group',
            name='users',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL, through='SecureWitness.UserToGroup'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='folder',
            name='GID',
            field=models.ForeignKey(to='SecureWitness.Group'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='folder',
            name='author_id',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='folder',
            name='parent',
            field=models.ForeignKey(null=True, blank=True, to='SecureWitness.Folder'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='file',
            name='report_id',
            field=models.ForeignKey(to='SecureWitness.Report'),
            preserve_default=True,
        ),
    ]
