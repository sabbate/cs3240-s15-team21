# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('SecureWitness', '0007_remove_reports_private'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reports',
            name='authorID',
        ),
        migrations.RemoveField(
            model_name='reports',
            name='folderID',
        ),
        migrations.AddField(
            model_name='reports',
            name='private',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
