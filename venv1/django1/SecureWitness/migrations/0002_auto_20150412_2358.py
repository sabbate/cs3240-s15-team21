# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('SecureWitness', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='files',
            name='content',
        ),
        migrations.RemoveField(
            model_name='files',
            name='id',
        ),
        migrations.AddField(
            model_name='files',
            name='docfile',
            field=models.FileField(upload_to='documents/', default='DEFAULT VALUE'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='files',
            name='fileID',
            field=models.AutoField(serialize=False, primary_key=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='reports',
            name='create_date',
            field=models.DateTimeField(),
            preserve_default=True,
        ),
    ]
