# Generated by Django 2.1.7 on 2019-05-12 20:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_base', '0012_cooperativa_email'),
    ]

    operations = [
        migrations.CreateModel(
            name='Telefone',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('telefone', models.CharField(max_length=30)),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_base.Cliente')),
                ('cooperativa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_base.Cooperativa')),
            ],
        ),
        migrations.RemoveField(
            model_name='endereco',
            name='telefone',
        ),
    ]