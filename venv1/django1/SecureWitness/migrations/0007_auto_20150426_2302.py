# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('auth', '0001_initial'),
        ('SecureWitness', '0006_auto_20150426_1812'),
    ]

    operations = [
        migrations.CreateModel(
            name='ReportGroupSharing',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('group', models.ForeignKey(to='auth.Group')),
                ('report', models.ForeignKey(to='SecureWitness.Report')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ReportUserSharing',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('report', models.ForeignKey(to='SecureWitness.Report')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RenameField(
            model_name='file',
            old_name='author_id',
            new_name='author',
        ),
        migrations.RenameField(
            model_name='file',
            old_name='report_id',
            new_name='report',
        ),
        migrations.AlterField(
            model_name='activationprofile',
            name='key_expires',
            field=models.DateTimeField(),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='report',
            name='create_date',
            field=models.DateTimeField(verbose_name='date created'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='report',
            name='last_update_date',
            field=models.DateTimeField(verbose_name='date of last modification'),
            preserve_default=True,
        ),
    ]
