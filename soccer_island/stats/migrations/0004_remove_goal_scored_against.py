# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stats', '0003_auto_20141031_1803'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='goal',
            name='scored_against',
        ),
    ]
