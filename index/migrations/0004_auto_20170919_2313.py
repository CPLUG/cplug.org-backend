# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-09-19 23:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0003_auto_20170919_2309'),
    ]

    operations = [
        migrations.AlterField(
            model_name='officer',
            name='picture',
            field=models.ImageField(blank=True, upload_to='/officers', verbose_name='Picture'),
        ),
    ]
