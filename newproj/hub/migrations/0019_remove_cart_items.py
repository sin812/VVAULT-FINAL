# Generated by Django 5.0.6 on 2024-07-16 15:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hub', '0018_vinyl_rating_cart_cartitem_cart_items_delete_review'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='items',
        ),
    ]