# Generated by Django 2.1 on 2018-08-24 22:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('usuario', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mensaje',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('asunto', models.CharField(max_length=50)),
                ('fecha_redaccion', models.DateTimeField(auto_now_add=True)),
                ('texto_mensaje', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Mensaje_Usuario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('leido', models.BooleanField(default=True)),
                ('mensaje', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='usuario.Mensaje')),
            ],
        ),
        migrations.AddField(
            model_name='usuario',
            name='activo',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='mensaje_usuario',
            name='receptor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='receptor', to='usuario.Usuario'),
        ),
        migrations.AddField(
            model_name='mensaje',
            name='emisor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='emisor', to='usuario.Usuario'),
        ),
    ]
