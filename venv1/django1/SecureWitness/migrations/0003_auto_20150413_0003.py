# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('SecureWitness', '0002_auto_20150412_2358'),
    ]

    operations = [
        migrations.AlterField(
            model_name='files',
            name='docfile',
            field=models.FileField(default=False, upload_to='documents/'),
            preserve_default=True,
        ),
    ]
