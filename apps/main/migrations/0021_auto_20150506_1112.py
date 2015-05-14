# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0020_auto_20150417_1538'),
    ]

    operations = [
        migrations.CreateModel(
            name='Empresa',
            fields=[
                ('emp_id', models.AutoField(serialize=False, primary_key=True)),
                ('emp_nom', models.CharField(max_length=250, blank=True)),
                ('emp_fec_exp_lic', models.DateField(null=True, blank=True)),
                ('emp_ver', models.CharField(max_length=6, blank=True)),
            ],
            options={
                'db_table': 'empresa',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Horario',
            fields=[
                ('hor_cod', models.AutoField(serialize=False, primary_key=True)),
                ('hor_lun', models.CharField(max_length=255, blank=True)),
                ('hor_mar', models.CharField(max_length=255, blank=True)),
                ('hor_mie', models.CharField(max_length=255, blank=True)),
                ('hor_jue', models.CharField(max_length=255, blank=True)),
                ('hor_vie', models.CharField(max_length=255, blank=True)),
                ('hor_sab', models.CharField(max_length=255, blank=True)),
                ('hor_dom', models.CharField(max_length=255, blank=True)),
            ],
            options={
                'db_table': 'horario',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.AlterModelOptions(
            name='eventos',
            options={'managed': False},
        ),
    ]
