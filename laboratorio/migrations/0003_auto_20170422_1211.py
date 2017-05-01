# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2017-04-22 17:11
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('laboratorio', '0002_auto_20170413_1626'),
    ]

    operations = [
        migrations.AlterField(
            model_name='experimento',
            name='proyecto',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='proyecto', to='laboratorio.Proyecto'),
        ),
        migrations.AlterField(
            model_name='experimento',
            name='responsable',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='responsable', to='laboratorio.Responsable'),
        ),
    ]