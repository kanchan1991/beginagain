# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-01-08 07:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0006_auto_20171214_1123'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='images',
            field=models.ImageField(default='profile_pictures/male.jpeg', null=True, upload_to='profile_pictures'),
        ),
    ]