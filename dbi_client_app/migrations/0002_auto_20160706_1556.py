# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-06 15:56
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dbi_client_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='dxinconexionconfiguracion',
            options={'managed': False},
        ),
        migrations.AlterModelOptions(
            name='dxinfiltros',
            options={'managed': False},
        ),
        migrations.AlterModelOptions(
            name='dxinindicadores',
            options={'managed': False},
        ),
        migrations.AlterModelOptions(
            name='dxinmapasclaves',
            options={'managed': False},
        ),
        migrations.AlterModelOptions(
            name='dxinproyectos',
            options={'managed': False},
        ),
        migrations.AlterModelOptions(
            name='dxinreglas',
            options={'managed': False},
        ),
        migrations.AlterModelOptions(
            name='dxinreglasindicadores',
            options={'managed': False},
        ),
    ]
