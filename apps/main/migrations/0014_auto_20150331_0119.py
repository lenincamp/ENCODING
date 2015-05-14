# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0013_auto_20150331_0053'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='submenu',
            name='men_cod',
        ),
        migrations.RemoveField(
            model_name='submenu',
            name='tip_cod',
        ),
        migrations.DeleteModel(
            name='SubMenu',
        ),
    ]
