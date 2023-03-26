# Generated by Django 4.1.7 on 2023-03-26 11:06

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='birthday',
            field=models.CharField(max_length=10, validators=[django.core.validators.RegexValidator('^\\d{2}\\.\\d{2}\\.\\d{4}$', 'Дата должна быть в формате dd.mm.yyyy')], verbose_name='День рождения'),
        ),
    ]