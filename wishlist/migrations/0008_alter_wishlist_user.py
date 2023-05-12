# Generated by Django 3.2.18 on 2023-05-12 10:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0002_auto_20230505_1603'),
        ('wishlist', '0007_alter_wishlistitem_wishlist'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wishlist',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='wishlist', to='profiles.userprofile'),
        ),
    ]
