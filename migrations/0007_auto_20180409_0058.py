# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-04-08 19:28
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pmsApp', '0006_auto_20180408_1919'),
    ]

    operations = [
        migrations.AlterField(
            model_name='application',
            name='DateOfBirth',
            field=models.DateField(default='1997-09-01'),
        ),
        migrations.AlterField(
            model_name='application',
            name='FirstName',
            field=models.CharField(default='sagar', max_length=30, validators=[django.core.validators.RegexValidator(message='Name should only contain characters', regex='^[a-zA-Z\\s]*$')]),
        ),
        migrations.AlterField(
            model_name='application',
            name='FlatNo',
            field=models.CharField(default='32', max_length=15),
        ),
        migrations.AlterField(
            model_name='application',
            name='LastName',
            field=models.CharField(default='sagar', max_length=30, validators=[django.core.validators.RegexValidator(message='Name should only contain characters', regex='^[a-zA-Z\\s]*$')]),
        ),
        migrations.AlterField(
            model_name='application',
            name='MiddleName',
            field=models.CharField(default='sagar', max_length=30, validators=[django.core.validators.RegexValidator(message='Name should only contain characters', regex='^[a-zA-Z\\s]*$')]),
        ),
        migrations.AlterField(
            model_name='application',
            name='PlaceOfBirth',
            field=models.CharField(default='somewhere', max_length=30),
        ),
    ]
