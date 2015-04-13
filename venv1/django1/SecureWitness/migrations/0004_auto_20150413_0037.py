# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('SecureWitness', '0003_auto_20150413_0003'),
    ]

    operations = [
        migrations.AlterField(
            model_name='files',
            name='docfile',
            field=models.FileField(default=False, upload_to='files/'),
            preserve_default=True,
        ),
    ]
