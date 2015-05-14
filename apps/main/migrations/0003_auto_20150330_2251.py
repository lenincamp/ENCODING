# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20150330_2250'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='detallemodulospermisos',
            table='detalle_modulos_permisos',
        ),
        migrations.AlterModelTable(
            name='modulos',
            table='modulos',
        ),
        migrations.AlterModelTable(
            name='permisos',
            table='permisos',
        ),
    ]
