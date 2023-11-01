# Generated by Django 4.2.5 on 2023-11-01 16:06

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("tube", "0006_video_uploader"),
    ]

    operations = [
        migrations.AlterField(
            model_name="video",
            name="uploader",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="videos",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
