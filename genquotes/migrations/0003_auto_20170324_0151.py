# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-24 01:51
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('genquotes', '0002_genquotes_author'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Genquotes',
            new_name='Quote',
        ),
        migrations.RenameField(
            model_name='quote',
            old_name='quote',
            new_name='quote_text',
        ),
    ]
