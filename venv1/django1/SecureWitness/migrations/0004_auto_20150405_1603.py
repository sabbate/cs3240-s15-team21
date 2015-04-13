# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('SecureWitness', '0003_auto_20150405_1410'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reports',
            name='id',
        ),
        migrations.AlterField(
            model_name='reports',
            name='RID',
            field=models.AutoField(primary_key=True, serialize=False),
            preserve_default=True,
        ),
    ]
