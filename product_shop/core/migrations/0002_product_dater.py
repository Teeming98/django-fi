# Generated by Django 4.1.5 on 2023-02-17 12:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='dater',
            field=models.DateField(default='2023-02-08', verbose_name='Дата изготавления'),
        ),
    ]
