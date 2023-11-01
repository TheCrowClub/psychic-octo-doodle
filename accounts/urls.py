from django.urls import path

from accounts.views import profile, signup, profileedit

urlpatterns = [
    path("signup/", signup, name="signup"),
    path("profile/", profile, name="profile"),
    path("profile/edit/", profileedit, name="profile_edit"),
]
