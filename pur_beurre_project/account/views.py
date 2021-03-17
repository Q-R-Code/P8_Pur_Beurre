from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import RegisterForm


# Create your views here.
def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/")
    else:
        form = RegisterForm()
    context = {"form": form}
    return render(request, "account/register.html", context)

def login(request):
    return render(request, 'registration/login.html')
