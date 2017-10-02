# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('price', '0007_auto_20170719_1824'),
    ]

    operations = [
        migrations.CreateModel(
            name='Other',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('ycluga', models.CharField(max_length=256, verbose_name='Услуга')),
                ('price', models.CharField(max_length=30, verbose_name='Цена')),
            ],
            options={
                'verbose_name_plural': 'Ногтевой сервис',
            },
        ),
        migrations.CreateModel(
            name='Other_type',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('Name', models.CharField(max_length=30)),
            ],
        ),
        migrations.AddField(
            model_name='other',
            name='type',
            field=models.ForeignKey(verbose_name='Вид', null=True, to='price.Other_type', blank=True),
        ),
    ]
