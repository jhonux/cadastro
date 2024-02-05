# Generated by Django 4.2.4 on 2023-08-26 12:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0003_remove_cliente_cpf_remove_cliente_email_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='cliente',
            name='email',
            field=models.EmailField(default='Desconhecido', max_length=254),
        ),
        migrations.AddField(
            model_name='veiculo',
            name='placa',
            field=models.CharField(default='Desconhecido', max_length=10),
        ),
        migrations.AlterModelTable(
            name='cliente',
            table=None,
        ),
        migrations.AlterModelTable(
            name='veiculo',
            table=None,
        ),
    ]
