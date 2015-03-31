# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0017_auto_20150331_0319'),
    ]

    operations = [
        migrations.AddField(
            model_name='submenu',
            name='sbm_men',
            field=models.NullBooleanField(),
            preserve_default=True,
        ),
    ]
