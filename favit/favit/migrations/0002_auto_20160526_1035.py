# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-26 17:35
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('favit', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fav',
            name='comment',
            field=models.CharField(blank=True, max_length=400, null=True),
        ),
        migrations.AlterField(
            model_name='fav',
            name='user_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
