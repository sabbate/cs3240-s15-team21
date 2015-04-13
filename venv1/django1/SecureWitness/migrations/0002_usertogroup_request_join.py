# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('SecureWitness', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='usertogroup',
            name='request_join',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
