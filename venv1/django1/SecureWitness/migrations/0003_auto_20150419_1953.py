# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('SecureWitness', '0002_activationprofile'),
    ]

    operations = [
        migrations.RenameField(
            model_name='activationprofile',
            old_name='username',
            new_name='user',
        ),
    ]
