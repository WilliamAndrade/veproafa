# Generated by Django 2.1.7 on 2019-05-02 02:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_base', '0005_remove_assinatura_data_pagamento'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assinatura',
            name='preco',
            field=models.DecimalField(decimal_places=3, max_digits=6),
        ),
    ]
