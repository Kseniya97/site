# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('price', '0005_auto_20170706_2243'),
    ]

    operations = [
        migrations.CreateModel(
            name='Man',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('ycluga', models.CharField(max_length=256, verbose_name='Услуга')),
                ('price', models.CharField(max_length=30, verbose_name='Цена')),
                ('dlinna', models.ForeignKey(to='price.Dlinna', null=True, blank=True, verbose_name='Длинна волос')),
            ],
        ),
        migrations.CreateModel(
            name='Woman',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('ycluga', models.CharField(max_length=256, verbose_name='Услуга')),
                ('price', models.CharField(max_length=30, verbose_name='Цена')),
                ('dlinna', models.ForeignKey(to='price.Dlinna', null=True, blank=True, verbose_name='Длинна волос')),
            ],
        ),
        migrations.RemoveField(
            model_name='price',
            name='dlinna',
        ),
        migrations.RemoveField(
            model_name='price',
            name='tipe',
        ),
        migrations.RemoveField(
            model_name='price',
            name='vid',
        ),
        migrations.DeleteModel(
            name='Price',
        ),
        migrations.DeleteModel(
            name='Tipe',
        ),
        migrations.DeleteModel(
            name='Vid',
        ),
    ]
