# Generated by Django 3.2.18 on 2023-05-16 17:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0004_alter_recipe_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='method',
            field=models.TextField(unique=True),
        ),
    ]
