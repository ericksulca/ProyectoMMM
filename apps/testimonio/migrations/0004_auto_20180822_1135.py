# Generated by Django 2.1 on 2018-08-22 16:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('testimonio', '0003_auto_20180822_1055'),
    ]

    operations = [
        migrations.RenameField(
            model_name='testimonio',
            old_name='usuario_id',
            new_name='usuario',
        ),
    ]