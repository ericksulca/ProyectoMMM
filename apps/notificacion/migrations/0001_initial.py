# Generated by Django 2.1 on 2018-09-27 05:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('usuario', '0005_remove_saldo_fecha_modificacion'),
    ]

    operations = [
        migrations.CreateModel(
            name='Notificacion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_receptor', models.IntegerField()),
                ('estado', models.IntegerField()),
                ('fecha_registro', models.DateTimeField(auto_now_add=True, null=True)),
                ('id_emisor', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='usuario.Usuario')),
            ],
        ),
    ]