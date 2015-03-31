# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0015_submenu'),
    ]

    operations = [
        migrations.AlterField(
            model_name='submenu',
            name='sbm_sbm',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
    ]
