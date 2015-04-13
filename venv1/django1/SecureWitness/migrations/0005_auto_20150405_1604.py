# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('SecureWitness', '0004_auto_20150405_1603'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reports',
            name='authorID',
            field=models.IntegerField(default='DEFAULT VALUE'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='reports',
            name='folderID',
            field=models.IntegerField(default='DEFAULT VALUE'),
            preserve_default=True,
        ),
    ]
