# Generated by Django 2.1 on 2018-10-25 17:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pago', '0007_auto_20181025_1135'),
    ]

    operations = [
        migrations.AddField(
            model_name='pago',
            name='monto_solicitado',
            field=models.DecimalField(decimal_places=2, max_digits=10, null=True),
        ),
    ]
