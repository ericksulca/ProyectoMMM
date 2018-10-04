# Generated by Django 2.1 on 2018-10-04 08:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('articulo', '0005_auto_20181004_0333'),
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.CharField(max_length=50, null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='articulo',
            name='fragmento',
        ),
        migrations.AddField(
            model_name='articulo',
            name='categoria',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.PROTECT, to='articulo.Categoria'),
            preserve_default=False,
        ),
    ]
