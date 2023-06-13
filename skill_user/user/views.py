from django.shortcuts import render, redirect
from .models import User
from .forms import UserForm
# Create your views here.

def list_user(request):
    users = User.objects.all()

    return render(request, "list_users.html", {"users": users})


def create_user(request):
    form = UserForm()
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("user-list")
    return render(request, "create_user.html", {"form": form})

def update_user():
    pass

def delete_user(request, pk):
    event = User.objects.get(pk=pk)
    event.delete()
    return redirect("user-list")
