# Generated by Django 2.1 on 2018-08-22 19:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testimonio', '0004_auto_20180822_1135'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testimonio',
            name='fecha_modificacion',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AlterField(
            model_name='testimonio',
            name='fecha_registro',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
