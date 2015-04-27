# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0001_initial'),
        ('SecureWitness', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ActivationProfile',
            fields=[
                ('activation_key', models.CharField(max_length=300, default='DEFAULT VALUE')),
                ('username', models.OneToOneField(serialize=False, primary_key=True, to=settings.AUTH_USER_MODEL)),
                ('key_expires', models.DateTimeField(default=datetime.date(2015, 4, 19))),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
