# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('SecureWitness', '0003_auto_20150402_1434'),
    ]

    operations = [
        migrations.AddField(
            model_name='report',
            name='report_name',
            field=models.CharField(max_length=200, default='Unnamed'),
            preserve_default=True,
        ),
    ]
