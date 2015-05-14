# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0016_auto_20150331_0308'),
    ]

    operations = [
        migrations.AlterField(
            model_name='submenu',
            name='sbm_sbm',
            field=models.IntegerField(null=True),
            preserve_default=True,
        ),
    ]
