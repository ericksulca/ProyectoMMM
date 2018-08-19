# Generated by Django 2.1 on 2018-08-19 17:07

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Entidad_bancaria',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('logo', models.ImageField(blank=True, upload_to='entidades_bancarias')),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('dni', models.IntegerField(primary_key=True, serialize=False, validators=[django.core.validators.MinValueValidator(10000000), django.core.validators.MaxValueValidator(99999999)])),
                ('nombres', models.CharField(max_length=50)),
                ('apellido_paterno', models.CharField(max_length=50)),
                ('apellido_materno', models.CharField(max_length=50)),
                ('foto_perfil', models.ImageField(blank=True, upload_to='usuario')),
                ('numero_cuenta', models.IntegerField(unique=True)),
                ('saldo', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=10)),
                ('dni_referido', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='usuario.Usuario')),
                ('entidad_bancaria', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='usuario.Entidad_bancaria')),
                ('usuario_login', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
