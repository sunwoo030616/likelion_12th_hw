# Generated by Django 5.0.3 on 2024-06-15 17:15

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("accounts", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="profile",
            name="followings",
            field=models.ManyToManyField(
                related_name="followers", to="accounts.profile"
            ),
        ),
    ]
