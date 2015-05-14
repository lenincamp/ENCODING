# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Asistencia',
            fields=[
                ('ast_cod', models.AutoField(serialize=False, primary_key=True)),
                ('cli_est', models.IntegerField(null=True, blank=True)),
            ],
            options={
                'db_table': 'asistencia',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('cat_cod', models.AutoField(serialize=False, primary_key=True)),
                ('cat_nom', models.CharField(max_length=100, blank=True)),
                ('cat_des', models.CharField(max_length=250, blank=True)),
                ('cat_est', models.NullBooleanField()),
                ('cat_url', models.CharField(max_length=250, blank=True)),
            ],
            options={
                'db_table': 'categoria',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Ciudad',
            fields=[
                ('ciu_cod', models.AutoField(serialize=False, primary_key=True)),
                ('ciu_nom', models.CharField(max_length=100, blank=True)),
            ],
            options={
                'db_table': 'ciudad',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('cli_nom', models.CharField(max_length=100, blank=True)),
                ('cli_ape', models.CharField(max_length=100, blank=True)),
                ('cli_tel', models.CharField(max_length=10, serialize=False, primary_key=True)),
                ('cli_dir', models.CharField(max_length=100, blank=True)),
                ('cli_eml', models.CharField(max_length=50, blank=True)),
            ],
            options={
                'db_table': 'cliente',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='DetalleSucursalEvento',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
            ],
            options={
                'db_table': 'detalle_sucursal_evento',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Eventos',
            fields=[
                ('eve_cod', models.AutoField(serialize=False, primary_key=True)),
                ('eve_nom', models.CharField(max_length=100, blank=True)),
                ('eve_fch', models.DateField(null=True, blank=True)),
                ('eve_inf', models.CharField(max_length=250, blank=True)),
                ('eve_url_img', models.CharField(max_length=250, blank=True)),
            ],
            options={
                'db_table': 'eventos',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='FormaPago',
            fields=[
                ('fpa_cod', models.AutoField(serialize=False, primary_key=True)),
                ('fpa_mes', models.IntegerField()),
                ('fpa_int', models.FloatField(null=True, blank=True)),
                ('fpa_prc_ent', models.FloatField(null=True, blank=True)),
                ('fpa_des', models.CharField(max_length=250, blank=True)),
            ],
            options={
                'db_table': 'forma_pago',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Mensaje',
            fields=[
                ('men_cod', models.AutoField(serialize=False, primary_key=True)),
                ('men_asu', models.CharField(max_length=100, blank=True)),
                ('men_crp', models.CharField(max_length=500, blank=True)),
                ('men_fch', models.DateField(null=True, blank=True)),
                ('men_est', models.NullBooleanField()),
            ],
            options={
                'db_table': 'mensaje',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Pieza',
            fields=[
                ('pie_cod', models.AutoField(serialize=False, primary_key=True)),
                ('pie_nom', models.CharField(max_length=100, blank=True)),
                ('pie_num', models.IntegerField(null=True, blank=True)),
            ],
            options={
                'db_table': 'pieza',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('prd_nom', models.CharField(max_length=150, blank=True)),
                ('prd_des', models.CharField(max_length=250, blank=True)),
                ('prd_pre', models.FloatField(null=True, blank=True)),
                ('prd_ofr', models.FloatField(null=True, blank=True)),
                ('prd_est', models.NullBooleanField()),
                ('prd_cod', models.AutoField(serialize=False, primary_key=True)),
                ('prd_url', models.CharField(max_length=250, blank=True)),
                ('prd_nro_piezas', models.IntegerField(null=True, blank=True)),
            ],
            options={
                'db_table': 'producto',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ProductoFpa',
            fields=[
                ('fpp_id', models.AutoField(serialize=False, primary_key=True)),
            ],
            options={
                'db_table': 'producto_fpa',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Sucursal',
            fields=[
                ('suc_cod', models.AutoField(serialize=False, primary_key=True)),
                ('suc_nom', models.CharField(max_length=100, blank=True)),
                ('suc_dir', models.CharField(max_length=100, blank=True)),
                ('suc_tel', models.CharField(max_length=10, blank=True)),
            ],
            options={
                'db_table': 'sucursal',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='TipoMensaje',
            fields=[
                ('tme_cod', models.AutoField(serialize=False, primary_key=True)),
                ('tme_des', models.CharField(max_length=100, blank=True)),
            ],
            options={
                'db_table': 'tipo_mensaje',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='TipoUsuario',
            fields=[
                ('tip_cod', models.AutoField(serialize=False, primary_key=True)),
                ('tip_des', models.CharField(max_length=50, blank=True)),
            ],
            options={
                'db_table': 'tipo_usuario',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('usu_cod', models.AutoField(serialize=False, primary_key=True)),
                ('usu_nom', models.CharField(max_length=100, blank=True)),
                ('usu_ape', models.CharField(max_length=100, blank=True)),
                ('usu_tel', models.CharField(max_length=10, blank=True)),
                ('usu_dir', models.CharField(max_length=150, blank=True)),
            ],
            options={
                'db_table': 'usuario',
                'managed': False,
            },
            bases=(models.Model,),
        ),
    ]
