# Generated by Django 4.2.5 on 2023-11-01 14:47

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("tube", "0004_comment_comment_date"),
    ]

    operations = [
        migrations.AlterField(
            model_name="comment",
            name="comment_date",
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]