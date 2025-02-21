# Generated by Django 5.1.6 on 2025-02-20 08:53

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='package',
            name='theme_id',
        ),
        migrations.AddField(
            model_name='theme',
            name='package_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='base.package'),
        ),
    ]
