# Generated by Django 2.1 on 2018-08-27 15:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuario', '0002_auto_20180824_1706'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='foto_perfil',
            field=models.ImageField(blank=True, default='usuario/Koala.jpg', upload_to='usuario'),
        ),
    ]