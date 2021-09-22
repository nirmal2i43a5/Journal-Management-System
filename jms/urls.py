"""jms URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from os import name
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path,include
from jms.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
      path('viewer/',include('viewer.urls',namespace='viewer')),
     path('accounts/login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('home/',dashboard, name = 'home'),
     path('user/',include('apps.user.urls',namespace='user')),
       path('reviewer/',include('apps.reviewer.urls',namespace='reviewer')),
        path('',include('apps.admin_user.urls',namespace='admin_app')),
     
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    
    