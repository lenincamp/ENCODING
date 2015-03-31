# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_menu_submenu'),
    ]

    operations = [
        migrations.AlterField(
            model_name='submenu',
            name='men_cod',
            field=models.ForeignKey(db_column=b'men_cod', blank=True, to='main.Menu', null=True),
            preserve_default=True,
        ),
    ]
