# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20150330_2251'),
    ]

    operations = [
        migrations.CreateModel(
            name='SubMenu',
            fields=[
                ('sbm_cod', models.AutoField(serialize=False, primary_key=True)),
                ('sbm_des', models.CharField(max_length=50)),
                ('sbm_sbm', models.IntegerField(null=True, blank=True)),
                ('tip_cod', models.ForeignKey(to='main.TipoUsuario', db_column=b'tip_cod')),
            ],
            options={
                'db_table': 'submenu',
            },
            bases=(models.Model,),
        ),
        migrations.RenameModel(
            old_name='Modulos',
            new_name='Menu',
        ),
        migrations.RemoveField(
            model_name='detallemodulospermisos',
            name='mod_cod',
        ),
        migrations.RemoveField(
            model_name='detallemodulospermisos',
            name='per_cod',
        ),
        migrations.RemoveField(
            model_name='detallemodulospermisos',
            name='tip_cod',
        ),
        migrations.DeleteModel(
            name='DetalleModulosPermisos',
        ),
        migrations.DeleteModel(
            name='Permisos',
        ),
        migrations.RenameField(
            model_name='menu',
            old_name='mod_cod',
            new_name='men_cod',
        ),
        migrations.RenameField(
            model_name='menu',
            old_name='mod_des',
            new_name='men_des',
        ),
        migrations.AlterModelTable(
            name='menu',
            table='menu',
        ),
    ]
