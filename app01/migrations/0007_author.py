# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-09-29 02:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0006_book_price'),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=32)),
                ('books', models.ManyToManyField(to='app01.Book')),
            ],
        ),
    ]