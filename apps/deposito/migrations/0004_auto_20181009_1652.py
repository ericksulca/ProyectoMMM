# Generated by Django 2.1 on 2018-10-09 21:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('deposito', '0003_auto_20181009_1649'),
    ]

    operations = [
        migrations.AlterField(
            model_name='operacion_backup',
            name='estado_backup',
            field=models.IntegerField(default=1),
        ),
    ]