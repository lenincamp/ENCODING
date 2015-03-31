# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0012_auto_20150331_0052'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menu',
            name='men_ico',
            field=models.CharField(max_length=25, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='submenu',
            name='sbm_des',
            field=models.CharField(max_length=50, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='submenu',
            name='sbm_ico',
            field=models.CharField(max_length=25, null=True),
            preserve_default=True,
        ),
    ]
