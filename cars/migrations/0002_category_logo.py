# Generated by Django 4.0.1 on 2022-01-22 08:33

import cars.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='logo',
            field=models.ImageField(null=True, upload_to=cars.models.get_file_name),
        ),
    ]