# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-06 23:17
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dbi_client_app', '0007_auto_20160706_2104'),
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
            options={'managed': True},
        ),
    ]
