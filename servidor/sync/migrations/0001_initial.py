# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-04-03 20:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Sync',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('table_name', models.CharField(max_length=200)),
                ('fecha_modificado', models.DateTimeField(verbose_name='Fecha Modificado')),
            ],
        ),
    ]
