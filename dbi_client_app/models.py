# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class AuthGroup(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    name = models.CharField(unique=True, max_length=160, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    name = models.CharField(max_length=510, blank=True, null=True)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    password = models.CharField(max_length=256, blank=True, null=True)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=60, blank=True, null=True)
    first_name = models.CharField(max_length=60, blank=True, null=True)
    last_name = models.CharField(max_length=60, blank=True, null=True)
    email = models.CharField(max_length=508, blank=True, null=True)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=400, blank=True, null=True)
    action_flag = models.IntegerField()
    change_message = models.TextField(blank=True, null=True)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    app_label = models.CharField(max_length=200, blank=True, null=True)
    model = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    app = models.CharField(max_length=510, blank=True, null=True)
    name = models.CharField(max_length=510, blank=True, null=True)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=80)
    session_data = models.TextField(blank=True, null=True)
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class DxinConexionConfiguracion(models.Model):
    id_conexionbd = models.IntegerField(primary_key=True)
    nb_servidor = models.CharField(max_length=200)
    nb_basedatos = models.CharField(max_length=200)
    nu_puerto = models.IntegerField()
    ti_basedatos = models.CharField(max_length=5)
    id_usuario = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    fh_carga = models.DateField()

    class Meta:
        managed = False
        db_table = 'dxin_conexion_configuracion'


class DxinFiltros(models.Model):
    id_proyecto = models.ForeignKey('DxinProyectos', models.DO_NOTHING, db_column='id_proyecto')
    id_filtro = models.CharField(primary_key=True, max_length=50)
    id_columna = models.CharField(max_length=50)
    sql = models.CharField(max_length=2000)
    valor_defecto = models.CharField(max_length=2000, blank=True, null=True)
    in_defecto = models.CharField(max_length=1)
    fh_carga = models.DateField()

    class Meta:
        managed = False
        db_table = 'dxin_filtros'


class DxinIndicadores(models.Model):
    id_proyecto = models.ForeignKey('DxinProyectos', models.DO_NOTHING, db_column='id_proyecto')
    id_indicador = models.CharField(primary_key=True, max_length=50)
    de_indicador = models.CharField(max_length=500)
    id_columna = models.CharField(max_length=50)
    ti_formato_numerico = models.CharField(max_length=50)
    fh_carga = models.DateField()
    in_predeterminado = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'dxin_indicadores'


class DxinMapasClaves(models.Model):
    id_proyecto = models.CharField(max_length=50)
    id_clave_mapa = models.CharField(max_length=100)
    id_columna = models.CharField(max_length=100)
    fh_carga = models.DateField()
    id_clave = models.FloatField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'dxin_mapas_claves'


class DxinProyectos(models.Model):
    id_proyecto = models.IntegerField(primary_key=True)
    de_proyecto = models.CharField(max_length=200)
    ti_dato_mostrar = models.CharField(max_length=5, blank=True, null=True)
    id_conexionbd = models.ForeignKey(DxinConexionConfiguracion, models.DO_NOTHING, db_column='id_conexionbd')
    sql = models.CharField(max_length=2000, blank=True, null=True)
    fh_carga = models.DateField()

    class Meta:
        managed = False
        db_table = 'dxin_proyectos'


class DxinReglas(models.Model):
    id_proyecto = models.CharField(max_length=100)
    id_indicador = models.CharField(max_length=50)
    ti_regla = models.CharField(max_length=5)
    fh_carga = models.DateField()
    id_regla = models.FloatField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'dxin_reglas'


class DxinReglasIndicadores(models.Model):
    id_proyecto = models.CharField(max_length=100)
    id_indicador = models.CharField(max_length=50)
    id_regla = models.IntegerField()
    orden = models.IntegerField()
    operador_logico = models.CharField(max_length=2)
    valor_referencia = models.CharField(max_length=20)
    ti_formato_trama = models.CharField(max_length=5, blank=True, null=True)
    ti_formato_activo = models.CharField(max_length=5, blank=True, null=True)
    ti_texto_color = models.CharField(max_length=5, blank=True, null=True)
    fh_carga = models.DateField()
    id_regla_ind = models.FloatField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'dxin_reglas_indicadores'
