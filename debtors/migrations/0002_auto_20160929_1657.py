# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-09-29 15:57
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('debtors', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Paylater_Debtors',
            new_name='Paylater_Debtor',
        ),
    ]
