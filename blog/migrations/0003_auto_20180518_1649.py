# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-05-18 11:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_post_new'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post_new',
            name='author',
            field=models.CharField(max_length=200),
        ),
    ]
