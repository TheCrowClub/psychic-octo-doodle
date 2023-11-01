from django.urls import path

from tube.views import createvideo, dashboard, detailvideo, list_video, search

urlpatterns = [
    path("", list_video, name="index"),
    path("create/", createvideo, name="create"),
    path("watch/<str:videoID>/", detailvideo, name="watch"),
    path("dashboard/", dashboard, name="dashboard"),
    path("search/", search, name="search"),
]
