# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-10-12 06:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MainFoodtypes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('typeid', models.CharField(max_length=20)),
                ('typename', models.CharField(max_length=20)),
                ('childtypenames', models.CharField(max_length=200)),
                ('typesort', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'axf_foodtypes',
            },
        ),
        migrations.CreateModel(
            name='MainGoods',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('productid', models.CharField(max_length=20)),
                ('productimg', models.CharField(max_length=200)),
                ('productname', models.CharField(max_length=200)),
                ('productlongname', models.CharField(max_length=50)),
                ('isxf', models.BooleanField()),
                ('pmdesc', models.IntegerField()),
                ('specifics', models.CharField(max_length=50)),
                ('price', models.FloatField()),
                ('marketprice', models.FloatField()),
                ('categoryid', models.IntegerField()),
                ('childcid', models.IntegerField()),
                ('childcidname', models.CharField(max_length=50)),
                ('dealerid', models.CharField(max_length=50)),
                ('storenums', models.IntegerField()),
                ('productnum', models.IntegerField()),
            ],
            options={
                'db_table': 'axf_goods',
            },
        ),
        migrations.CreateModel(
            name='MainMustBuy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.CharField(max_length=200)),
                ('name', models.CharField(max_length=20)),
                ('trackid', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'axf_mustbuy',
            },
        ),
        migrations.CreateModel(
            name='MainNav',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.CharField(max_length=200)),
                ('name', models.CharField(max_length=20)),
                ('trackid', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'axf_nav',
            },
        ),
        migrations.CreateModel(
            name='MainShop',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.CharField(max_length=200)),
                ('name', models.CharField(max_length=20)),
                ('trackid', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'axf_shop',
            },
        ),
        migrations.CreateModel(
            name='MainShow',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.CharField(max_length=200)),
                ('name', models.CharField(max_length=20)),
                ('trackid', models.CharField(max_length=20)),
                ('categoryid', models.CharField(max_length=20)),
                ('brandname', models.CharField(max_length=20)),
                ('img1', models.CharField(max_length=200)),
                ('childcid1', models.CharField(max_length=20)),
                ('productid1', models.CharField(max_length=20)),
                ('longname1', models.CharField(max_length=100)),
                ('price1', models.CharField(max_length=20)),
                ('marketprice1', models.CharField(max_length=20)),
                ('img2', models.CharField(max_length=200)),
                ('childcid2', models.CharField(max_length=20)),
                ('productid2', models.CharField(max_length=20)),
                ('longname2', models.CharField(max_length=100)),
                ('price2', models.CharField(max_length=20)),
                ('marketprice2', models.CharField(max_length=20)),
                ('img3', models.CharField(max_length=200)),
                ('childcid3', models.CharField(max_length=20)),
                ('productid3', models.CharField(max_length=20)),
                ('longname3', models.CharField(max_length=100)),
                ('price3', models.CharField(max_length=20)),
                ('marketprice3', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'axf_mainshow',
            },
        ),
        migrations.CreateModel(
            name='MainWheel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.CharField(max_length=200)),
                ('name', models.CharField(max_length=20)),
                ('trackid', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'axf_wheel',
            },
        ),
    ]
