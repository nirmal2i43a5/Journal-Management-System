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
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('viewer/',include('viewer.urls',namespace='viewer')),
     
     path('accounts/login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('dashboard/',dashboard, name = 'home'),
      path('',first_page, name = 'first_page'),
     path('user/',include('apps.user.urls',namespace='user')),
       path('reviewer/',include('apps.reviewer.urls',namespace='reviewer')),
        path('',include('apps.admin_user.urls',namespace='admin_app')),
        #  path('authentication/',include('apps.authentication.urls',namespace='authentication')),
        path('permission/',include('apps.permissions.urls',namespace='role_app')),
          path('',include('apps.authentication.urls')),
          
              #For resetting password via email follow below four link 
    path('password/reset/',auth_views.PasswordResetView.as_view(template_name = 'passwordreset/password_reset_email.html'), 
		 name = "password_reset"),
	
	path('password/reset/done/',auth_views.PasswordResetDoneView.as_view(template_name = 'passwordreset/password_reset_sent.html'), 
		 name = "password_reset_done"),
	
	path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name='passwordreset/password_reset_form.html'),
		 name="password_reset_confirm"),  
	   
	 #<token> check  for valid user or not--><uidb64> user id encoded in base 64--this email is sent to the user
	 #<uidb64> helps to know user who request for password
	path('reset/complete/',auth_views.PasswordResetCompleteView.as_view(template_name='passwordreset/password_reset_complete.html'),
		 name="password_reset_complete"),
     
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    
    