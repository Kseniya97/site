# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('price', '0003_auto_20170705_2147'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='price',
            options={'verbose_name': 'Прайс-лист', 'verbose_name_plural': 'Прайс-лист'},
        ),
        migrations.AddField(
            model_name='price',
            name='comment',
            field=models.TextField(verbose_name='Комментарий', null=True),
        ),
    ]
