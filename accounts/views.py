from django.shortcuts import redirect, render

from accounts import forms

# Create your views here.


def signup(request):
    if request.user.is_authenticated:
        return redirect("dashboard")
    form = forms.UserCreationForm()
    if request.method == "POST":
        form = forms.UserCreationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("/dashboard/")
    return render(
        request,
        template_name="accounts/signup.html",
        context={"form": form},
    )


def profile(request):
    if not request.user.is_authenticated:
        return redirect("/accounts/login/")
    return render(request, template_name="accounts/profile.html")


def profileedit(request):
    if not request.user.is_authenticated:
        return redirect("/accounts/login/")
    form = forms.ChangeProfile(instance=request.user)
    if request.method == "POST":
        form = forms.ChangeProfile(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect("/accounts/profile/")
    return render(
        request, template_name="accounts/editprofile.html", context={"form": form}
    )
