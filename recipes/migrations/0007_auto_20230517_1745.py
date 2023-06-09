# Generated by Django 3.2.18 on 2023-05-17 17:45

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0006_alter_recipe_method'),
    ]

    operations = [
        migrations.RenameField(
            model_name='recipe',
            old_name='brew_time_mins',
            new_name='brew_time',
        ),
        migrations.RenameField(
            model_name='recipe',
            old_name='coffee_qty_g',
            new_name='coffee_qty',
        ),
        migrations.RenameField(
            model_name='recipe',
            old_name='water_temp_c',
            new_name='water_temp',
        ),
        migrations.RenameField(
            model_name='recipe',
            old_name='water_volume_ml',
            new_name='water_volume',
        ),
        migrations.AlterField(
            model_name='recipe',
            name='intro',
            field=models.TextField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
