# Generated by Django 2.1 on 2018-08-27 16:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usuario', '0004_auto_20180827_1120'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='saldo',
            name='fecha_modificacion',
        ),
    ]