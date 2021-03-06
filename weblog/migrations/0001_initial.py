# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-08-07 08:24
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=200)),
                ('favorite', models.BooleanField()),
                ('comment', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('User_name', models.CharField(max_length=200)),
                ('password', models.CharField(max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name='post',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='weblog.Users'),
        ),
    ]
