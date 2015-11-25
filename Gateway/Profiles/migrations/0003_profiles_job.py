# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Profiles', '0002_profiles_location'),
    ]

    operations = [
        migrations.AddField(
            model_name='profiles',
            name='job',
            field=models.CharField(max_length=1200, null=True),
        ),
    ]
