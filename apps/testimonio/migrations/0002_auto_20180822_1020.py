# Generated by Django 2.1 on 2018-08-22 15:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testimonio', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testimonio',
            name='contenido',
            field=models.CharField(max_length=200),
        ),
    ]