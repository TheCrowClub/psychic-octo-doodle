# Generated by Django 4.2.5 on 2023-11-01 15:45

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("tube", "0005_alter_comment_comment_date"),
    ]

    operations = [
        migrations.AddField(
            model_name="video",
            name="uploader",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="videos",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
