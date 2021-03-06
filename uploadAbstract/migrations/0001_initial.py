# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-06-10 13:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = {
        migrations.CreateModel(
            name='SubmittedAbstract',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('salutation', models.CharField(max_length=6)),
                ('first_name', models.CharField(max_length=35)),
                ('last_name', models.CharField(max_length=35)),
                ('co_authors_names', models.CharField(max_length=770)),
                ('email', models.EmailField(max_length=60, unique=True)),
                ('paper_title', models.CharField(max_length=300)),
                ('abstract', models.CharField(max_length=2000)),
            ],
        ),
    }
