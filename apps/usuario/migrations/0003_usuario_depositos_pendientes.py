# Generated by Django 2.1 on 2018-10-11 17:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuario', '0002_auto_20181010_1202'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='depositos_pendientes',
            field=models.IntegerField(null=True),
        ),
    ]