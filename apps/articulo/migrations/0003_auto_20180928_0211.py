# Generated by Django 2.1 on 2018-09-28 07:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articulo', '0002_auto_20180831_0009'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articulo',
            name='contenido',
            field=models.TextField(),
        ),
    ]
