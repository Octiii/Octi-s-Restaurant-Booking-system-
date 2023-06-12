# Generated by Django 3.2.18 on 2023-06-12 13:43

import cloudinary.models
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('reservation', '0009_dish'),
    ]

    operations = [
        migrations.AddField(
            model_name='dish',
            name='created_on',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='dish',
            name='featured_image',
            field=cloudinary.models.CloudinaryField(default='palceholder', max_length=255, verbose_name='image'),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='persons',
            field=models.BigIntegerField(blank=True, default='0'),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='phone',
            field=models.BigIntegerField(blank=True, default='0'),
        ),
    ]