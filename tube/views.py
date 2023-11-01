from django.db.models import Q

from django.shortcuts import get_object_or_404, redirect, render

from tube.forms import CommentForm, VideoForm
from tube.models import Comment, Video


# Create your views here.
def list_video(request, page=1):
    videos = Video.objects.all()
    return render(
        request,
        template_name="tube/videolist.html",
        context={
            "videos": videos,
        },
    )


def createvideo(request):
    if not request.user.is_authenticated:
        return redirect("/accounts/login/")
    form = VideoForm()
    if request.method == "POST":
        form = VideoForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.uploader = request.user
            form.save()
            return redirect(form)
    return render(request, template_name="tube/create.html", context={"form": form})


def detailvideo(request, videoID):
    video = get_object_or_404(Video, videoID=videoID)
    comments = video.comments.all()
    commentform = CommentForm()
    if request.method == "POST":
        commentform = CommentForm(request.POST)
        commentform.author = request.user
        if commentform.is_valid():
            comment = Comment(
                author=request.user, video=video, comment=request.POST.get("comment")
            )
            comment.save()

            return redirect("watch", videoID=videoID)
    return render(
        request,
        template_name="tube/video.html",
        context={"video": video, "commentform": commentform, "comments": comments},
    )


def dashboard(request):
    if not request.user.is_authenticated:
        return redirect("/accounts/login/")
    query = Video.objects.filter(uploader=request.user)
    return render(
        request, template_name="tube/dashboard.html", context={"videos": query}
    )


def search(request):
    query = request.GET.get("query", "")
    if not query:
        pass
    print(query)
    videos = Video.objects.filter(
        Q(title__icontains=query) | Q(description__icontains=query)
    )
    return render(
        request,
        template_name="tube/search.html",
        context={"videos": videos, "query": query},
    )
