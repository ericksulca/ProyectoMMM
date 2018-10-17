# Generated by Django 2.1 on 2018-10-17 16:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuario', '0005_usuario_fecha'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='id',
            field=models.AutoField(auto_created=True, default=4, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='usuario',
            name='dni',
            field=models.IntegerField(unique=True),
        ),
    ]
