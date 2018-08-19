# Generated by Django 2.1 on 2018-08-19 17:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('usuario', '0001_initial'),
        ('solicitud', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Operaciones',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('monto', models.DecimalField(decimal_places=2, max_digits=10)),
                ('fecha', models.DateTimeField(auto_now=True)),
                ('estado', models.BooleanField(default=True)),
                ('tipo_movimiento', models.CharField(choices=[('retiro', 'Retiro'), ('deposito', 'Depósito')], max_length=8)),
                ('solicitud', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='solicitud.Solicitud')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='UsuarioPaga', to='usuario.Usuario')),
                ('usuario_asignado', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='UsuarioAsignado', to='usuario.Usuario')),
            ],
        ),
        migrations.CreateModel(
            name='OperacionesBackUp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('monto_backup', models.DecimalField(decimal_places=2, max_digits=10)),
                ('fecha_backup', models.DateTimeField(auto_now=True)),
                ('estado_backup', models.BooleanField(default=True)),
                ('tipo_movimiento_backup', models.CharField(choices=[('retiro', 'Retiro'), ('deposito', 'Depósito')], max_length=8)),
                ('solicitud_backup', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='solicitud.Solicitud')),
                ('usuario_asignado_backup', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='UsuarioAsignadoBackUp', to='usuario.Usuario')),
                ('usuario_backup', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='UsuarioPagaBackUp', to='usuario.Usuario')),
            ],
        ),
    ]
