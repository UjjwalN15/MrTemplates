# Generated by Django 5.1.6 on 2025-02-20 08:08

import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Package',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('price', models.IntegerField()),
                ('package_duration', models.CharField(blank=True, max_length=255, null=True)),
                ('package_type', models.CharField(choices=[('basic', 'Basic'), ('mid level', 'Mid Level'), ('advanced', 'Advanced')], max_length=255)),
                ('is_active', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='StoreCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Theme',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('image', models.ImageField(upload_to='theme_images/')),
                ('url', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('username', models.CharField(blank=True, max_length=225, null=True)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('password', models.CharField(max_length=225)),
                ('is_active', models.BooleanField(default=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('role', models.ForeignKey(blank=True, default=3, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='custom_user_roles', to='auth.group')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Store',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('store_logo', models.ImageField(upload_to='store_logo/')),
                ('store_description', models.TextField()),
                ('theme_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.package')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('store_category_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.storecategory')),
            ],
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.IntegerField()),
                ('payment_method', models.CharField(choices=[('Esewa', 'Esewa'), ('Khalti', 'Khalti'), ('IME Pay', 'IME Pay'), ('Bank Transfer', 'Bank Transfer'), ('Cash On Delivery', 'Cash On Delivery')], max_length=255)),
                ('payment_status', models.CharField(choices=[('Paid', 'Paid'), ('Unpaid', 'Unpaid'), ('Pending', 'Pending')], default='Unpaid', max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('package_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.package')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('store_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.store')),
            ],
        ),
        migrations.AddField(
            model_name='package',
            name='theme_id',
            field=models.ManyToManyField(related_name='themes', to='base.theme'),
        ),
    ]
