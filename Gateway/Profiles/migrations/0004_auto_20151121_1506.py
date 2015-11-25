# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Profiles', '0003_profiles_job'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profiles',
            name='job',
        ),
        migrations.RemoveField(
            model_name='profiles',
            name='location',
        ),
    ]
