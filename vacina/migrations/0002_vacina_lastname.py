# Generated by Django 2.2 on 2021-09-01 18:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vacina', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='vacina',
            name='lastName',
            field=models.CharField(default=1, max_length=100, verbose_name='lastName'),
            preserve_default=False,
        ),
    ]
