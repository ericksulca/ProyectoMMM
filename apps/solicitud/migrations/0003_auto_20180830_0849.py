# Generated by Django 2.1 on 2018-08-30 13:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('solicitud', '0002_solicitud_pagado'),
    ]

    operations = [
        migrations.RenameField(
            model_name='solicitud',
            old_name='fecha_confirmacion',
            new_name='fecha_modificacion',
        ),
    ]
