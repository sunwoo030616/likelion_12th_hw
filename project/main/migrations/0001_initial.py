# Generated by Django 5.0.3 on 2024-04-11 15:00

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Post",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=50)),
                ("writer", models.CharField(max_length=30)),
                ("weather", models.CharField(max_length=20)),
                ("body", models.TextField()),
                ("pub_date", models.DateTimeField()),
            ],
        ),
    ]