# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('SecureWitness', '0008_auto_20150405_1611'),
    ]

    operations = [
        migrations.AddField(
            model_name='reports',
            name='authorID',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='reports',
            name='folderID',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
    ]
