# Generated by Django 2.2 on 2021-10-24 19:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vacina', '0017_auto_20211024_1920'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='cpf',
            field=models.CharField(default='CPF', max_length=14, verbose_name='CPF'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='endereco',
            field=models.CharField(default='Endereço', max_length=100, verbose_name='Endereço'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='telefone',
            field=models.CharField(default='Telefone', max_length=11, verbose_name='Telefone'),
        ),
    ]
