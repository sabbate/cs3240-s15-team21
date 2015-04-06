# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('SecureWitness', '0003_user_email'),
    ]

    operations = [
        migrations.CreateModel(
            name='ReportSharingGroup',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('sharing_date', models.DateTimeField(verbose_name=datetime.datetime(2015, 4, 6, 16, 41, 23, 742129))),
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
                ('sharing_date', models.DateTimeField(verbose_name=datetime.datetime(2015, 4, 6, 16, 41, 23, 741129))),
                ('UID', models.ForeignKey(to='SecureWitness.User')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='report',
            name='file',
            field=models.CharField(default='DEFAULT VALUE', max_length=300),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='report',
            name='incident_date',
            field=models.CharField(default='DEFAULT VALUE', max_length=300),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='report',
            name='keywords',
            field=models.CharField(default='DEFAULT VALUE', max_length=300),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='report',
            name='location',
            field=models.CharField(default='DEFAULT VALUE', max_length=300),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='report',
            name='long_desc',
            field=models.CharField(default='DEFAULT VALUE', max_length=300),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='report',
            name='private',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='report',
            name='short_desc',
            field=models.CharField(default='DEFAULT VALUE', max_length=150),
            preserve_default=True,
        ),
    ]
