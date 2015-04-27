# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0001_initial'),
        ('SecureWitness', '0005_auto_20150421_1929'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reportsharinggroup',
            name='group_id',
        ),
        migrations.DeleteModel(
            name='ReportSharingGroup',
        ),
        migrations.RemoveField(
            model_name='reportsharinguser',
            name='user_id',
        ),
        migrations.DeleteModel(
            name='ReportSharingUser',
        ),
        migrations.AddField(
            model_name='report',
            name='group_id',
            field=models.ForeignKey(blank=True, null=True, to='auth.Group'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='activationprofile',
            name='key_expires',
            field=models.DateTimeField(default=datetime.datetime(2015, 4, 26, 18, 12, 23, 864682)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='report',
            name='create_date',
            field=models.DateTimeField(verbose_name='date created', default=datetime.datetime(2015, 4, 26, 18, 12, 23, 864683)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='report',
            name='folder_id',
            field=models.ForeignKey(blank=True, null=True, to='SecureWitness.Folder'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='report',
            name='last_update_date',
            field=models.DateTimeField(verbose_name='date of last modification', default=datetime.datetime(2015, 4, 26, 18, 12, 23, 864683)),
            preserve_default=True,
        ),
    ]
