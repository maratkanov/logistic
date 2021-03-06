# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-12 20:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='RequestModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=30)),
                ('company', models.CharField(blank=True, max_length=30)),
                ('phone', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=30)),
                ('ship_date', models.DateTimeField()),
                ('from_address', models.CharField(blank=True, max_length=30)),
                ('to_address', models.CharField(blank=True, max_length=30)),
                ('price', models.PositiveIntegerField(blank=True, null=True)),
                ('amount', models.PositiveIntegerField(blank=True, null=True)),
                ('weight', models.PositiveIntegerField(blank=True, null=True)),
                ('code', models.PositiveIntegerField(blank=True, null=True)),
                ('size', models.PositiveIntegerField(blank=True, null=True)),
                ('places', models.PositiveIntegerField(blank=True, null=True)),
                ('is_seen', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='SimpleRequestModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=30)),
                ('email', models.EmailField(max_length=30)),
                ('phone', models.CharField(max_length=30)),
                ('is_seen', models.BooleanField(default=False)),
            ],
        ),
    ]
