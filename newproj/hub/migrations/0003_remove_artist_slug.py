# Generated by Django 5.0.6 on 2024-06-30 09:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hub', '0002_alter_vinyl_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='artist',
            name='slug',
        ),
    ]
