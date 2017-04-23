# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2017-04-22 18:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('laboratorio', '0006_auto_20170422_1329'),
    ]

    operations = [
        migrations.AlterField(
            model_name='responsable',
            name='celular',
            field=models.BigIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='responsable',
            name='email',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.RemoveField(
            model_name='patrocinador',
            name='celular',
        ),
        migrations.AddField(
            model_name='patrocinador',
            name='email',
            field=models.CharField(default='', max_length=200),
        ),
    ]