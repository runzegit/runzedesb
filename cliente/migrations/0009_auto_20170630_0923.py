# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-30 12:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cliente', '0008_auto_20170613_1041'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='datDesb',
            field=models.DateField(blank=True, null=True, verbose_name='\xdaltimo Desbloqueio'),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='diaVen',
            field=models.IntegerField(blank=True, null=True, verbose_name='Dia Vencimento'),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='mesRef',
            field=models.IntegerField(blank=True, null=True, verbose_name='M\xeas Refer\xeancia'),
        ),
    ]