# Generated by Django 3.2.18 on 2023-05-21 19:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0007_alter_order_postcode'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='postcode',
            field=models.CharField(max_length=8),
        ),
    ]
