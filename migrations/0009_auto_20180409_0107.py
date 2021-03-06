# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-04-08 19:37
from __future__ import unicode_literals

from django.db import migrations, models
import pmsApp.models


class Migration(migrations.Migration):

    dependencies = [
        ('pmsApp', '0008_auto_20180409_0058'),
    ]

    operations = [
        migrations.AlterField(
            model_name='documents',
            name='AddressProof',
            field=models.ImageField(upload_to=pmsApp.models.get_address_folder, validators=[pmsApp.models.validate_file_extension]),
        ),
        migrations.AlterField(
            model_name='documents',
            name='BirthCertificate',
            field=models.ImageField(upload_to=pmsApp.models.get_birth_certificate_folder, validators=[pmsApp.models.validate_file_extension]),
        ),
        migrations.AlterField(
            model_name='documents',
            name='PaymentReceipt',
            field=models.ImageField(upload_to=pmsApp.models.get_payment_receipt_folder, validators=[pmsApp.models.validate_file_extension]),
        ),
    ]
