# Generated by Django 4.2.16 on 2024-11-05 15:03

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0010_remove_cart_quantity"),
    ]

    operations = [
        migrations.AddField(
            model_name="message",
            name="created_at",
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
