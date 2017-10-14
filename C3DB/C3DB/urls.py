"""C3DB URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf import settings
from django.contrib.auth.views import login, logout
from django.contrib.auth import views as auth_views
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.contrib import admin
from .views import SignUp, UserCreateDoneTV

urlpatterns = [
    # - admin page
    url(r'^admin/', include(admin.site.urls)),

    # - index app
    url(r'^C3DB/', include('index.urls', namespace='C3DB', app_name='index')),

    # - Django: user login page
    url('^accounts/login/$', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),

    # - Django: user logout page
    url('^accounts/logout/$', auth_views.LogoutView.as_view(template_name='registration/logout.html'), name='logout'),

    # - Django: user register page
    url(r'^accounts/register/$', SignUp, name='register'),
    # - Django: user register done page
#    url(r'^accounts/register_done/$', UserCreateDoneTV.as_view(), name='register_done'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
