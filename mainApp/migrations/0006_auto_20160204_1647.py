# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-02-04 16:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0005_remove_item_order'),
    ]

    operations = [
        migrations.AlterField(
            model_name='infopage',
            name='slug',
            field=models.SlugField(),
        ),
    ]
