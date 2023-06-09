# Generated by Django 3.2.18 on 2023-05-15 10:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_alter_product_category'),
        ('favourites', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='favouriteslistitem',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='favourite_products', to='products.product'),
        ),
    ]
