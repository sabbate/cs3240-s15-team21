# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('SecureWitness', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='reports',
            name='filepath',
            field=models.CharField(default='DEFAULT VALUE', max_length=300),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='reports',
            name='long_desc',
            field=models.CharField(default='DEFAULT VALUE', max_length=300),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='reports',
            name='short_desc',
            field=models.CharField(default='DEFAULT VALUE', max_length=150),
            preserve_default=True,
        ),
    ]
