# Generated by Django 4.2.6 on 2023-11-01 19:53

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("accounts", "0006_remove_user_age"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="user",
            name="profile_pic",
        ),
    ]
