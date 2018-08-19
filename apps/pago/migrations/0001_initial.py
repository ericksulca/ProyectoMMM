# Generated by Django 2.1 on 2018-08-18 02:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('usuario', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pago',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('monto', models.DecimalField(decimal_places=2, max_digits=10)),
                ('fecha', models.DateTimeField(auto_now=True)),
                ('estado', models.BooleanField(default=True)),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='UsuarioPaga', to='usuario.Usuario')),
                ('usuario_asignado', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='UsuarioAsignado', to='usuario.Usuario')),
            ],
        ),
    ]
