# Generated by Django 2.2 on 2021-10-24 19:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vacina', '0016_auto_20211013_1557'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='Comorbidade',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='alergia',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='cidade',
        ),
        migrations.AddField(
            model_name='profile',
            name='nome',
            field=models.CharField(default='Nome', max_length=100, verbose_name='Nome'),
        ),
    ]
