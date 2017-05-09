# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models

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
        db_table = 'dxin_conexion_configuracion'

class DxinFiltros(models.Model):
    id_proyecto = models.ForeignKey('DxinProyectos', db_column='id_proyecto')
    id_filtro = models.CharField(primary_key=True, max_length=50)
    id_columna = models.CharField(max_length=50)
    sql = models.CharField(max_length=2000)
    valor_defecto = models.CharField(max_length=2000)
    in_defecto = models.CharField(max_length=1)
    fh_carga = models.DateField()
    ti_valor = models.CharField(max_length=5, default='')
    de_columna = models.CharField(max_length=50, default='')

    class Meta:
        db_table = 'dxin_filtros'

class DxinIndicadores(models.Model):
    id_proyecto = models.ForeignKey('DxinProyectos', db_column='id_proyecto')
    id_indicador = models.CharField(primary_key=True, max_length=50)
    de_indicador = models.CharField(max_length=500)
    id_columna = models.CharField(max_length=50)
    ti_formato_numerico = models.CharField(max_length=50)
    fh_carga = models.DateField()
    in_predeterminado = models.CharField(max_length=1)

    class Meta:
        db_table = 'dxin_indicadores'

class DxinMapasClaves(models.Model):
    id_proyecto = models.CharField(max_length=50)
    id_clave_mapa = models.CharField(max_length=100)
    id_columna = models.CharField(max_length=100)
    fh_carga = models.DateField()
    id_clave = models.FloatField(primary_key=True)

    class Meta:
        db_table = 'dxin_mapas_claves'

class DxinProyectos(models.Model):
    id_proyecto = models.IntegerField(primary_key=True)
    de_proyecto = models.CharField(max_length=200)
    ti_dato_mostrar = models.CharField(max_length=5, blank=True, null=True)
    id_conexionbd = models.ForeignKey(DxinConexionConfiguracion, models.DO_NOTHING, db_column='id_conexionbd')
    sql = models.CharField(max_length=2000, blank=True, null=True)
    fh_carga = models.DateField()

    class Meta:
        db_table = 'dxin_proyectos'

class DxinReglas(models.Model):
    id_proyecto = models.CharField(max_length=100)
    id_indicador = models.CharField(max_length=50)
    ti_regla = models.CharField(max_length=5)
    fh_carga = models.DateField()
    id_regla = models.FloatField(primary_key=True)

    class Meta:
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
        db_table = 'dxin_reglas_indicadores'