# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('SecureWitness', '0002_auto_20150401_2242'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Files',
            new_name='File',
        ),
        migrations.RenameModel(
            old_name='Folders',
            new_name='Folder',
        ),
        migrations.RenameModel(
            old_name='Reports',
            new_name='Report',
        ),
        migrations.RenameModel(
            old_name='Users',
            new_name='User',
        ),
        migrations.RenameModel(
            old_name='UsersInGroups',
            new_name='UserToGroup',
        ),
    ]
