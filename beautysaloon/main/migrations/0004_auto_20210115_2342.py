# Generated by Django 3.1.5 on 2021-01-15 20:42

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_discount'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='visits',
            name='date',
        ),
        migrations.AddField(
            model_name='visits',
            name='price',
            field=models.IntegerField(default=1, validators=[django.core.validators.MinValueValidator(1)], verbose_name='Цена'),
        ),
    ]
