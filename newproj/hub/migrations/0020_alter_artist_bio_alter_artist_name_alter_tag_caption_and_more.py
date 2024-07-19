# Generated by Django 5.0.6 on 2024-07-16 21:21

import django.core.validators
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hub', '0019_remove_cart_items'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='artist',
            name='bio',
            field=models.TextField(help_text='Enter the biography of the artist'),
        ),
        migrations.AlterField(
            model_name='artist',
            name='name',
            field=models.CharField(help_text='Enter the artist name', max_length=50),
        ),
        migrations.AlterField(
            model_name='tag',
            name='caption',
            field=models.CharField(help_text='Enter tag caption', max_length=20),
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score', models.IntegerField(help_text='Rate the vinyl from 1 to 10', validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(10)])),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('vinyl', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ratings', to='hub.vinyl')),
            ],
        ),
        migrations.DeleteModel(
            name='Customer',
        ),
    ]
