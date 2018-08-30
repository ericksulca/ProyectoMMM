# Generated by Django 2.1 on 2018-08-22 13:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('usuario', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Testimonio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contenido', models.CharField(max_length=500)),
                ('usuario_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='usuario.Usuario')),
            ],
        ),
    ]