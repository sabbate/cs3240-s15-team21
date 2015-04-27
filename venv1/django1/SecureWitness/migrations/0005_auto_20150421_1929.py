# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0001_initial'),
        ('SecureWitness', '0004_auto_20150420_1814'),
    ]

    operations = [
        migrations.CreateModel(
            name='GroupProfile',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('datetime', models.DateTimeField(verbose_name='date created')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='group',
            name='users',
        ),
        migrations.AddField(
            model_name='groupprofile',
            name='group',
            field=models.OneToOneField(to='auth.Group'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='activationprofile',
            name='key_expires',
            field=models.DateTimeField(default=datetime.date(2015, 4, 21)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='folder',
            name='GID',
            field=models.ForeignKey(to='auth.Group'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='reportsharinggroup',
            name='group_id',
            field=models.ForeignKey(to='auth.Group'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='usertogroup',
            name='group_id',
            field=models.ForeignKey(to='auth.Group'),
            preserve_default=True,
        ),
        migrations.DeleteModel(
            name='Group',
        ),
    ]
