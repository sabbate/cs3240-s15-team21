# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('SecureWitness', '0006_auto_20150402_1722'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='UserToGroup',
            new_name='UsersInGroups',
        ),
    ]
