from django import forms

from tube.models import Comment, Video


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ("comment",)


class VideoForm(forms.ModelForm):
    class Meta:
        model = Video
        fields = (
            "title",
            "videoID",
            "description",
        )
