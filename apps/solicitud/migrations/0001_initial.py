# Generated by Django 2.1 on 2018-11-15 14:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('usuario', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Solicitud',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateTimeField(auto_now_add=True)),
                ('fecha_modificacion', models.DateTimeField(auto_now=True)),
                ('monto', models.DecimalField(decimal_places=2, max_digits=10)),
                ('monto_completado', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('monto_faltante', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('confirmacion', models.BooleanField(default=False)),
                ('pagado', models.BooleanField(default=False)),
                ('estado', models.BooleanField(default=True)),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='usuario.Usuario')),
            ],
        ),
    ]
