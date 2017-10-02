# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('price', '0004_auto_20170706_1315'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tipe',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('Name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Vid',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('Name', models.CharField(max_length=30)),
            ],
        ),
        migrations.RenameModel(
            old_name='Category',
            new_name='Dlinna',
        ),
        migrations.RemoveField(
            model_name='price',
            name='category',
        ),
        migrations.RemoveField(
            model_name='price',
            name='comment',
        ),
        migrations.AddField(
            model_name='price',
            name='dlinna',
            field=models.ForeignKey(to='price.Dlinna', null=True, blank=True, verbose_name='Длинна волос'),
        ),
        migrations.AlterField(
            model_name='price',
            name='Price',
            field=models.CharField(max_length=30, verbose_name='Цена'),
        ),
        migrations.AlterField(
            model_name='price',
            name='Ycluga',
            field=models.CharField(max_length=256, verbose_name='Услуга'),
        ),
        migrations.AddField(
            model_name='price',
            name='tipe',
            field=models.ForeignKey(to='price.Tipe', null=True, blank=True, verbose_name='Тип услуги'),
        ),
        migrations.AddField(
            model_name='price',
            name='vid',
            field=models.ForeignKey(to='price.Vid', null=True, blank=True, verbose_name='Вид услуги'),
        ),
    ]
