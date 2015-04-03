# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('SecureWitness', '0007_auto_20150402_1726'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserToGroup',
            fields=[
                ('ID', models.AutoField(serialize=False, primary_key=True)),
                ('leader', models.BooleanField(default=False)),
                ('GID', models.ManyToManyField(to='SecureWitness.Group')),
                ('UID', models.ManyToManyField(to='SecureWitness.User')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='usersingroups',
            name='GID',
        ),
        migrations.RemoveField(
            model_name='usersingroups',
            name='UID',
        ),
        migrations.DeleteModel(
            name='UsersInGroups',
        ),
    ]
