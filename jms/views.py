

from django.shortcuts import render, get_object_or_404


def dashboard(request):
    context = {
        'title':'Dashboard'
    }
    return render(request, 'dashboard.html',context)


