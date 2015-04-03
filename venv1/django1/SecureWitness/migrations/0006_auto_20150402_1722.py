# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('SecureWitness', '0005_auto_20150402_1705'),
    ]

    operations = [
        migrations.AlterField(
            model_name='report',
            name='report_name',
            field=models.CharField(max_length=200),
            preserve_default=True,
        ),
    ]
