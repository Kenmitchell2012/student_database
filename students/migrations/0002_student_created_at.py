# Generated by Django 4.1.10 on 2023-09-25 02:47

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):
    dependencies = [
        ("students", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="student",
            name="created_at",
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
