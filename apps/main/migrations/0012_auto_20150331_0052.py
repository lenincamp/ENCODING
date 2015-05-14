# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0011_auto_20150331_0020'),
    ]

    operations = [
        migrations.AlterField(
            model_name='submenu',
            name='sbm_des',
            field=models.CharField(max_length=50, blank=True),
            preserve_default=True,
        ),
    ]
