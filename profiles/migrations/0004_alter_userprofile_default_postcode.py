# Generated by Django 3.2.18 on 2023-05-21 19:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0003_alter_userprofile_default_postcode'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='default_postcode',
            field=models.CharField(blank=True, max_length=8, null=True),
        ),
    ]
