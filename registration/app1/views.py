from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .views import authview, home

def authview(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/accounts/login/")  # <-- this sends user to login page
    else:
        form = UserCreationForm()  # blank form for GET requests

    return render(request, "registration/signup.html", {"form": form})
