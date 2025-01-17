# Generated by Django 5.0.6 on 2024-07-15 21:03

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hub', '0016_review'),
    ]

    operations = [
        migrations.RenameField(
            model_name='review',
            old_name='created_at',
            new_name='date_added',
        ),
        migrations.AlterField(
            model_name='review',
            name='comment',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='review',
            name='rating',
            field=models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)]),
        ),
    ]
