# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('price', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='price',
            options={'verbose_name_plural': 'Прайс-лист', 'verbose_name': 'Прайс-лист'},
        ),
        migrations.AlterField(
            model_name='price',
            name='Price',
            field=models.CharField(max_length=10),
        ),
    ]
