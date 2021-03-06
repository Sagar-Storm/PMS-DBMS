# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-04-08 13:32
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pmsApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='documents',
            name='ApplicantId',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='pmsApp.Applicant'),
        ),
        migrations.AlterField(
            model_name='status',
            name='ApplicantId',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='pmsApp.Applicant'),
        ),
    ]
