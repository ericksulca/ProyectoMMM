# Generated by Django 2.1 on 2018-09-27 07:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notificacion', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='notificacion',
            name='tipo',
            field=models.CharField(default=100, max_length=100),
            preserve_default=False,
        ),
    ]
