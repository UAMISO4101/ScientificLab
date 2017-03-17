# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2017-03-15 23:44
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('laboratorio', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Elemento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=250, null=True)),
                ('cantidad', models.FloatField(null=True)),
                ('unidades', models.IntegerField(choices=[(0, 'Centimetros'), (1, 'Gramos'), (2, 'Centimetros cubicos'), (3, 'Unidades')], null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Experimento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=250, null=True)),
                ('descripcion', models.CharField(max_length=1000, null=True)),
                ('fechaInicio', models.DateField(null=True)),
                ('prioridad', models.IntegerField(null=True)),
                ('estado', models.IntegerField(choices=[(0, 'Iniciado'), (1, 'Terminado')], null=True)),
                ('resultado', models.IntegerField(choices=[(0, 'Exitoso'), (1, 'Fallido')], null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Paso',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=250, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Patrocinador',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=250, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Protocolo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=250, null=True)),
                ('descripcion', models.CharField(max_length=1000, null=True)),
                ('version', models.IntegerField(null=True)),
                ('categoria', models.IntegerField(choices=[(0, 'Hongos'), (1, 'Bacterias'), (2, 'Extraccion ADN'), (3, 'Pruebas Biologicas')], null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ProtocolosExperimento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('experimento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='laboratorio.Experimento')),
                ('protocolo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='laboratorio.Protocolo')),
            ],
        ),
        migrations.CreateModel(
            name='Proyecto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=250, null=True)),
                ('descripcion', models.CharField(max_length=1000, null=True)),
                ('fechaInicio', models.DateField(null=True)),
                ('fechaFinal', models.DateField(null=True)),
                ('prioridad', models.IntegerField(null=True)),
                ('avance', models.FloatField(null=True)),
                ('estado', models.IntegerField(choices=[(0, 'Iniciado'), (1, 'Terminado'), (2, 'En Progreso'), (3, 'Cancelado'), (4, 'Pausado')], null=True)),
                ('patrocinador', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='proyectos', to='laboratorio.Patrocinador')),
            ],
        ),
        migrations.CreateModel(
            name='Responsable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=250, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='protocolo',
            name='experimentos',
            field=models.ManyToManyField(through='laboratorio.ProtocolosExperimento', to='laboratorio.Experimento'),
        ),
        migrations.AddField(
            model_name='paso',
            name='protocolos',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='pasos', to='laboratorio.Protocolo'),
        ),
        migrations.AddField(
            model_name='experimento',
            name='proyecto',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='experimentos', to='laboratorio.Proyecto'),
        ),
        migrations.AddField(
            model_name='experimento',
            name='responsable',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='experimentos', to='laboratorio.Responsable'),
        ),
        migrations.AddField(
            model_name='elemento',
            name='pasos',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='elementos', to='laboratorio.Paso'),
        ),
    ]
