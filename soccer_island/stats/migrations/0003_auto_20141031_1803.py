# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stats', '0002_auto_20141031_1753'),
    ]

    operations = [
        migrations.AlterField(
            model_name='club',
            name='logo',
            field=models.ImageField(null=True, upload_to=b'', blank=True),
        ),
    ]
