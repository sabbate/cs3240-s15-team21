# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('SecureWitness', '0003_auto_20150419_1953'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usertogroup',
            name='request_join',
        ),
        migrations.AlterField(
            model_name='activationprofile',
            name='key_expires',
            field=models.DateTimeField(default=datetime.date(2015, 4, 20)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='folder',
            name='parent',
            field=models.ForeignKey(null=True, blank=True, to='SecureWitness.Folder'),
            preserve_default=True,
        ),
    ]
