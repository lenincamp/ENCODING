# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_auto_20150330_2334'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='submenu',
            name='tip_cod',
        ),
        migrations.DeleteModel(
            name='SubMenu',
        ),
    ]
