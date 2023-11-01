# Generated by Django 4.2.6 on 2023-10-29 18:44

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Video",
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
                ("title", models.CharField(max_length=250, verbose_name="Video Title")),
                (
                    "videoID",
                    models.CharField(max_length=20, verbose_name="Youtube Video Id"),
                ),
                (
                    "description",
                    models.TextField(verbose_name="Description of the Video"),
                ),
            ],
        ),
    ]
