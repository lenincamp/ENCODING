# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0018_submenu_sbm_men'),
    ]

    operations = [
        migrations.AlterField(
            model_name='submenu',
            name='sbm_sbm',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
    ]
