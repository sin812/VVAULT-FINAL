from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from .forms import RegisterForm
from .decorators import unauthenticated_user
from django.contrib.auth.models import Group
from django.contrib.auth.decorators import login_required


def userpage(request):
    context={}
    return render(request, 'userpage.html', context)

@unauthenticated_user
def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user=form.save()
            # Optionally, log in the user after registration
            username = form.cleaned_data.get('username')
            group = Group.objects.get(name='UnprivUser')
            user.groups.add(group)
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            # Add a success message
            messages.success(request, "Account created successfully")
            # Redirect to a success page or home page
            return redirect('index')  # Replace 'index' with your desired URL name
    else:
        form = RegisterForm()
    return render(request, "register/register.html", {"form": form})

@unauthenticated_user
def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('index')  # Replace 'index' with your desired URL name
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    else:
        form = AuthenticationForm()
    return render(request, "registration/login.html", {"form": form})

def logout_view(request):
    logout(request)
    return redirect('login')  # Replace 'index' with your desired URL name

