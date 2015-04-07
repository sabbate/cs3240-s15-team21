# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('SecureWitness', '0009_auto_20150405_1612'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reports',
            name='RID',
            field=models.IntegerField(serialize=False, primary_key=True),
            preserve_default=True,
        ),
    ]
