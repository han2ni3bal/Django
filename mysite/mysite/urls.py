"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include
from users import views
from django.urls import re_path


app_name='users'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index),
    re_path(r'^register/$',views.register,name='register'),
    re_path(r'^login/$',views.login,name='login'),
    re_path(r'^article/$',views.article),
    #re_path(r'^detail',views.detail,name='detail'),
    re_path(r'^article/(?P<id>\d+)/$',views.detail,name='detail'),
    #path('accounts/',include('app_name.urls')),
    re_path(r'^user/(?P<pk>\d+)/profile/$',views.profile,name='profile'),
   # re_path(r'^user/(?P<pk>\d+)/profile/update/$',views.profile_update,name='profile_update'),
    #re_path(r'^user/(?P<pk>\d+)/pwdchange/$', views.pwd_change,name='pwd_change'),
    re_path(r'^logout/$',views.logout,name='logout'),
]
