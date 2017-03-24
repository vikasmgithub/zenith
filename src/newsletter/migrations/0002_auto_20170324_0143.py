# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('newsletter', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='signup',
            name='contact_no',
            field=models.CharField(max_length=240, null=True),
        ),
        migrations.AddField(
            model_name='signup',
            name='location',
            field=models.CharField(max_length=240, null=True),
        ),
    ]
