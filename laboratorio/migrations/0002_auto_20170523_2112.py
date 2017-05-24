# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2017-05-24 02:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('laboratorio', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='protocolo',
            name='habilitado',
            field=models.NullBooleanField(),
        ),
        migrations.AlterField(
            model_name='protocolo',
            name='descripcion',
            field=models.TextField(max_length=1000, null=True),
        ),
    ]
