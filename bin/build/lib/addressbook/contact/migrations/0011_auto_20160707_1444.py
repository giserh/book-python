# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-07 14:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0010_auto_20160707_1444'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='photo',
            field=models.FileField(null=True, upload_to='', verbose_name='Photo'),
        ),
    ]
