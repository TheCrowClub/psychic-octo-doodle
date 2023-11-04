from datetime import datetime

from django.db import models
from django.urls import reverse

from accounts.models import User


class Categories(models.TextChoices):
    MUSIC = "MUSIC", "Music"
    ANIFILM = "ANIFILM", "Animation and Film"
    PETS = "PETS", "Pets and Animals"
    SPORTS = "SPORTS", "Sports"
    GAMING = "GAMING", "Gaming"
    NEWS = "NEWS", "News"
    POLITICS = "POLITICS", "Politics"
    EDUCATION = "EDUCATION", "Education"
    SCINECEANDTECH = "SCITECH", "Science And Technology"
    OTHERS = "OTHERS", "Others"


class Video(models.Model):
    uploader = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="videos",
    )
    title = models.CharField(verbose_name="Video Title", max_length=250)
    videoID = models.CharField(
        verbose_name="Youtube Video Id", max_length=20, primary_key=True
    )
    category = models.CharField(
        max_length=30, choices=Categories.choices, default=Categories.OTHERS
    )
    description = models.TextField(verbose_name="Description of the Video")

    def get_absolute_url(self):
        return reverse("watch", args=[self.videoID])

    def __str__(self):
        return self.title


class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    video = models.ForeignKey(Video, on_delete=models.CASCADE, related_name="comments")
    comment = models.TextField(verbose_name="Your Comment")
    comment_date = models.DateTimeField(
        auto_now_add=True,
    )

    def __str__(self):
        return self.comment
