# Generated by Django 5.1.6 on 2025-02-20 08:53

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_remove_package_theme_id_theme_package_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='theme',
            name='package_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.package'),
        ),
    ]
