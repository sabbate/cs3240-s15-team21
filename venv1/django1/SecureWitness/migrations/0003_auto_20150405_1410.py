# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('SecureWitness', '0002_auto_20150330_1457'),
    ]

    operations = [
        migrations.AddField(
            model_name='reports',
            name='incident_date',
            field=models.CharField(max_length=300, default='DEFAULT VALUE'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='reports',
            name='keywords',
            field=models.CharField(max_length=300, default='DEFAULT VALUE'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='reports',
            name='location',
            field=models.CharField(max_length=300, default='DEFAULT VALUE'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='reports',
            name='private',
            field=models.BooleanField(default=0),
            preserve_default=True,
        ),
    ]
