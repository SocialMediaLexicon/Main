# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2022-06-10 10:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('social_app', '0002_auto_20220610_1008'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='blog_pic',
            field=models.ImageField(blank=True, null=True, upload_to='blog_pics'),
        ),
    ]
