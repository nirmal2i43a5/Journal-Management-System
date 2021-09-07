

from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import LoginForm


def dashboard(request):
    context = {
        'title': 'Dashboard'
    }
    return render(request, 'dashboard.html', context)


def user_login(request):

    form = LoginForm()

    if request.method == "POST":
        
        username = request.POST.get("username")
        password = request.POST.get("password1")
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            group = None
            if request.user.groups.exists():
                group = request.user.groups.all()[0].name
            if group or request.user.is_superuser:
                return redirect('home')
            else:
                messages.error(request, "Invalid User")
                return redirect('login')
        else:
            messages.error(request, "Invalid Login Details")
            return redirect('login')

    return render(request, 'login.html', {'form': form})



def user_logout(request):
    logout(request)
    return redirect('login')
