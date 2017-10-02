# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('price', '0006_auto_20170719_1214'),
    ]

    operations = [
        migrations.CreateModel(
            name='Nails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ycluga', models.CharField(max_length=256, verbose_name='Услуга')),
                ('price', models.CharField(max_length=30, verbose_name='Цена')),
            ],
            options={
                'verbose_name_plural': 'Ногтевой сервис',
            },
        ),
        migrations.CreateModel(
            name='Nails_type',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=30)),
            ],
        ),
        migrations.AlterModelOptions(
            name='man',
            options={'verbose_name_plural': 'Мужской зал'},
        ),
        migrations.AlterModelOptions(
            name='woman',
            options={'verbose_name_plural': 'Женский зал'},
        ),
        migrations.AddField(
            model_name='nails',
            name='type',
            field=models.ForeignKey(to='price.Nails_type', blank=True, verbose_name='Вид', null=True),
        ),
    ]
