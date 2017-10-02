# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('price', '0002_auto_20170705_1326'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('Name', models.CharField(max_length=30)),
            ],
        ),
        migrations.AlterModelOptions(
            name='price',
            options={},
        ),
        migrations.AlterField(
            model_name='price',
            name='Price',
            field=models.CharField(max_length=30),
        ),
        migrations.AddField(
            model_name='price',
            name='category',
            field=models.ForeignKey(null=True, verbose_name='Категория', to='price.Category', blank=True),
        ),
    ]
