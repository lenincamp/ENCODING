# Create your models here.
from django.db import models


class Asistencia(models.Model):
    ast_cod = models.AutoField(primary_key=True)
    det_suc_eve_cod = models.ForeignKey('DetalleSucursalEvento', db_column='det_suc_eve_cod')
    cli_tel = models.ForeignKey('Cliente', db_column='cli_tel', blank=True, null=True)
    cli_est = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'asistencia'


class Categoria(models.Model):
    cat_cod = models.AutoField(primary_key=True)
    cat_nom = models.CharField(max_length=100, blank=True)
    cat_des = models.CharField(max_length=250, blank=True)
    cat_est = models.NullBooleanField()
    cat_url = models.ImageField(upload_to='images',max_length=250, blank=True)
    emp_id = models.ForeignKey('Empresa', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'categoria'


class Ciudad(models.Model):
    ciu_cod = models.AutoField(primary_key=True)
    ciu_nom = models.CharField(max_length=100, blank=True)

    class Meta:
        managed = False
        db_table = 'ciudad'


class Cliente(models.Model):
    cli_nom = models.CharField(max_length=100, blank=True)
    cli_ape = models.CharField(max_length=100, blank=True)
    cli_tel = models.CharField(primary_key=True, max_length=10)
    cli_dir = models.CharField(max_length=100, blank=True)
    cli_eml = models.CharField(max_length=50, blank=True)
    emp = models.ForeignKey('Empresa', blank=True, null=True)
    cli_id = models.IntegerField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'cliente'


class DetalleSucursalEvento(models.Model):
    id = models.AutoField(primary_key=True)
    eve_cod = models.ForeignKey('Eventos', db_column='eve_cod')
    suc_cod = models.ForeignKey('Sucursal', db_column='suc_cod')
    eve_fch = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'detalle_sucursal_evento'

class Empresa(models.Model):
    emp_id = models.AutoField(primary_key=True)
    emp_nom = models.CharField(max_length=250, blank=True)
    emp_fec_exp_lic = models.DateField(blank=True, null=True)
    emp_ver = models.CharField(max_length=6, blank=True)

    class Meta:
        managed = False
        db_table = 'empresa'


class Eventos(models.Model):
    eve_cod = models.AutoField(primary_key=True)
    eve_nom = models.CharField(max_length=100, blank=True)
    eve_fch = models.DateField(blank=True, null=True)
    eve_inf = models.CharField(max_length=250, blank=True)
    eve_url_img = models.ImageField(upload_to='images', blank=True)
    emp = models.ForeignKey(Empresa, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'eventos'


class FormaPago(models.Model):
    fpa_cod = models.AutoField(primary_key=True)
    fpa_mes = models.IntegerField()
    fpa_int = models.FloatField(blank=True, null=True)
    fpa_prc_ent = models.FloatField(blank=True, null=True)
    fpa_des = models.CharField(max_length=250, blank=True)

    class Meta:
        managed = False
        db_table = 'forma_pago'

class Horario(models.Model):
    hor_cod = models.AutoField(primary_key=True)
    hor_lun = models.CharField(max_length=255, blank=True)
    hor_mar = models.CharField(max_length=255, blank=True)
    hor_mie = models.CharField(max_length=255, blank=True)
    hor_jue = models.CharField(max_length=255, blank=True)
    hor_vie = models.CharField(max_length=255, blank=True)
    hor_sab = models.CharField(max_length=255, blank=True)
    hor_dom = models.CharField(max_length=255, blank=True)
    suc_cod = models.ForeignKey('Sucursal', db_column='suc_cod', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'horario'


class Mensaje(models.Model):
    men_cod = models.AutoField(primary_key=True)
    men_asu = models.CharField(max_length=100, blank=True)
    men_crp = models.CharField(max_length=500, blank=True)
    men_fch = models.DateField(blank=True, null=True)
    men_est = models.NullBooleanField()
    tme_cod = models.ForeignKey('TipoMensaje', db_column='tme_cod')
    usu_cod = models.ForeignKey('Usuario', db_column='usu_cod')
    cli = models.ForeignKey(Cliente, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mensaje'


class Pieza(models.Model):
    pie_cod = models.AutoField(primary_key=True)
    pie_nom = models.CharField(max_length=100, blank=True)
    prd_cod = models.ForeignKey('Producto', db_column='prd_cod')
    pie_num = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pieza'


class Producto(models.Model):
    prd_nom = models.CharField(max_length=150, blank=True)
    prd_des = models.CharField(max_length=250, blank=True)
    prd_pre = models.FloatField(blank=True, null=True)
    prd_ofr = models.FloatField(blank=True, null=True)
    prd_est = models.NullBooleanField()
    cat_cod = models.ForeignKey(Categoria, db_column='cat_cod', blank=True, null=True)
    prd_cod = models.AutoField(primary_key=True)
    prd_url = models.ImageField(upload_to='images',max_length=250, blank=True)
    prd_nro_piezas = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'producto'


class ProductoFpa(models.Model):
    fpp_id = models.AutoField(primary_key=True)
    prd_cod = models.ForeignKey(Producto, db_column='prd_cod')
    fpa_cod = models.ForeignKey(FormaPago, db_column='fpa_cod')

    class Meta:
        managed = False
        db_table = 'producto_fpa'


class Sucursal(models.Model):
    suc_cod = models.AutoField(primary_key=True)
    suc_nom = models.CharField(max_length=100, blank=True)
    suc_dir = models.CharField(max_length=100, blank=True)
    suc_tel = models.CharField(max_length=10, blank=True)
    ciu_cod = models.ForeignKey(Ciudad, db_column='ciu_cod')
    suc_lat = models.FloatField(blank=True, null=True)
    suc_lng = models.FloatField(blank=True, null=True)
    emp = models.ForeignKey(Empresa, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sucursal'


class TipoMensaje(models.Model):
    tme_cod = models.AutoField(primary_key=True)
    tme_des = models.CharField(max_length=100, blank=True)

    class Meta:
        managed = False
        db_table = 'tipo_mensaje'


class TipoUsuario(models.Model):
    tip_cod = models.AutoField(primary_key=True)
    tip_des = models.CharField(max_length=50, blank=True)

    class Meta:
        managed = False
        db_table = 'tipo_usuario'


class Usuario(models.Model):
    usu_cod  = models.AutoField(primary_key=True)
    usu_nom  = models.CharField(max_length=100, blank=True)
    usu_ape  = models.CharField(max_length=100, blank=True)
    usu_tel  = models.CharField(max_length=10, blank=True)
    usu_dir  = models.CharField(max_length=150, blank=True)
    tip_cod  = models.ForeignKey(TipoUsuario, db_column='tip_cod')
    usu_pass = models.CharField(max_length=16)
    usu_ced  = models.CharField(max_length=10)

    class Meta:
        managed = False
        db_table = 'usuario'

class Menu(models.Model):
    men_cod = models.AutoField(primary_key=True)
    men_des = models.CharField(max_length=50)
    men_ico = models.CharField(max_length=25, null=True)
    class Meta:
        db_table = 'menu'

class SubMenu(models.Model):
    sbm_cod = models.AutoField(primary_key=True)
    sbm_des = models.CharField(max_length=50, null=True)
    sbm_ico = models.CharField(max_length=25, null=True)
    sbm_url = models.CharField(max_length=150)
    #codigo de submenu (menu)
    sbm_sbm = models.IntegerField(default=0)
    sbm_men = models.NullBooleanField()
    men_cod = models.ForeignKey(Menu, db_column='men_cod', blank=True,null=True)
    tip_cod = models.ForeignKey(TipoUsuario, db_column='tip_cod')
    class Meta:
        db_table = 'submenu'