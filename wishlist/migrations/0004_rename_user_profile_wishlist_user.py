# Generated by Django 3.2.18 on 2023-05-11 16:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wishlist', '0003_rename_added_on_wishlist_date'),
    ]

    operations = [
        migrations.RenameField(
            model_name='wishlist',
            old_name='user_profile',
            new_name='user',
        ),
    ]
