# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DetalleModulosPermisos',
            fields=[
                ('dmp_cod', models.AutoField(serialize=False, primary_key=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Modulos',
            fields=[
                ('mod_cod', models.AutoField(serialize=False, primary_key=True)),
                ('mod_des', models.CharField(max_length=50)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Permisos',
            fields=[
                ('per_cod', models.AutoField(serialize=False, primary_key=True)),
                ('per_des', models.CharField(max_length=50)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='detallemodulospermisos',
            name='mod_cod',
            field=models.ForeignKey(to='main.Modulos', db_column=b'mod_cod'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='detallemodulospermisos',
            name='per_cod',
            field=models.ForeignKey(to='main.Permisos', db_column=b'per_cod'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='detallemodulospermisos',
            name='tip_cod',
            field=models.ForeignKey(db_column=b'tip_cod', blank=True, to='main.TipoUsuario', null=True),
            preserve_default=True,
        ),
    ]
