# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-22 23:06
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pharmacy', '0002_medicalequipment_medicine_supplies'),
    ]

    operations = [
        migrations.AddField(
            model_name='supplies',
            name='measuring_unit',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='pharmacy.MeasuringUnit', verbose_name='Unidad de Medida'),
            preserve_default=False,
        ),
    ]