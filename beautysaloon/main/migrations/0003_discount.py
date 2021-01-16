# Generated by Django 3.1.5 on 2021-01-15 19:55

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20210115_2249'),
    ]

    operations = [
        migrations.CreateModel(
            name='Discount',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('discountcode', models.IntegerField(unique=True, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(9999999)], verbose_name='Код акции')),
                ('discountname', models.CharField(max_length=250, verbose_name='Название акции')),
                ('description', models.TextField(blank=True, verbose_name='Описание акции')),
            ],
            options={
                'verbose_name': 'Акция',
                'verbose_name_plural': 'Акции',
            },
        ),
    ]
