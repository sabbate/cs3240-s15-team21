# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('SecureWitness', '0010_auto_20150405_1613'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reports',
            name='RID',
            field=models.AutoField(primary_key=True, serialize=False),
            preserve_default=True,
        ),
    ]
