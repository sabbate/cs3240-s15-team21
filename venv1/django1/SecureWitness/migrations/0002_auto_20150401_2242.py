# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('SecureWitness', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UsersInGroups',
            fields=[
                ('ID', models.AutoField(primary_key=True, serialize=False)),
                ('leader', models.BooleanField(default=False)),
                ('GID', models.ManyToManyField(to='SecureWitness.Group')),
                ('UID', models.ManyToManyField(to='SecureWitness.Users')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.DeleteModel(
            name='Users_in_groups',
        ),
        migrations.RemoveField(
            model_name='files',
            name='id',
        ),
        migrations.RemoveField(
            model_name='folders',
            name='id',
        ),
        migrations.RemoveField(
            model_name='group',
            name='id',
        ),
        migrations.RemoveField(
            model_name='reports',
            name='id',
        ),
        migrations.RemoveField(
            model_name='users',
            name='id',
        ),
        migrations.RemoveField(
            model_name='users',
            name='privilege',
        ),
        migrations.AddField(
            model_name='users',
            name='admin',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='files',
            name='fileID',
            field=models.AutoField(primary_key=True, serialize=False),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='folders',
            name='folderID',
            field=models.AutoField(primary_key=True, serialize=False),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='group',
            name='GID',
            field=models.AutoField(primary_key=True, serialize=False),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='reports',
            name='RID',
            field=models.AutoField(primary_key=True, serialize=False),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='reports',
            name='folderID',
            field=models.ForeignKey(to='SecureWitness.Files'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='users',
            name='UID',
            field=models.AutoField(primary_key=True, serialize=False),
            preserve_default=True,
        ),
    ]
