# Generated by Django 4.1.5 on 2023-02-24 08:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.ImageField(default='static/images/placeholder.png', upload_to=''),
        ),
    ]
