# Generated by Django 4.2.4 on 2023-08-24 01:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='veiculo',
            name='ano',
            field=models.IntegerField(blank=True),
        ),
    ]
