# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-11 18:50
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Online',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('domain', models.CharField(max_length=30)),
            ],
        ),
        migrations.AlterModelTable(
            name='dreamreal',
            table='online',
        ),
        migrations.AddField(
            model_name='dreamreal',
            name='online',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='myapp.Online'),
        ),
    ]
