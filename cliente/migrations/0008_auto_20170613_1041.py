# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-13 13:41
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cliente', '0007_cliente_mesref'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cliente',
            old_name='email',
            new_name='telefone',
        ),
    ]