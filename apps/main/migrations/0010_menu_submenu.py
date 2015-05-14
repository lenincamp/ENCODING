# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_auto_20150330_2358'),
    ]

    operations = [
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('men_cod', models.AutoField(serialize=False, primary_key=True)),
                ('men_des', models.CharField(max_length=50)),
                ('men_ico', models.CharField(max_length=25, null=True, blank=True)),
            ],
            options={
                'db_table': 'menu',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='SubMenu',
            fields=[
                ('sbm_cod', models.AutoField(serialize=False, primary_key=True)),
                ('sbm_des', models.CharField(max_length=50)),
                ('sbm_ico', models.CharField(max_length=25, null=True, blank=True)),
                ('sbm_sbm', models.IntegerField(null=True, blank=True)),
                ('men_cod', models.ForeignKey(to='main.Menu', db_column=b'men_cod')),
                ('tip_cod', models.ForeignKey(to='main.TipoUsuario', db_column=b'tip_cod')),
            ],
            options={
                'db_table': 'submenu',
            },
            bases=(models.Model,),
        ),
    ]
