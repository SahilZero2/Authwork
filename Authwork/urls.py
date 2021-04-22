"""Authwork URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path,include
from userwork.views import profile
from blog.views import blog , blogpost ,AddPostView,UpdatePostView , DeletePostView
from django.conf.urls.static import static
from django.conf import settings



urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('userwork.urls')),
    path('accounts',include('django.contrib.auth.urls')),
    path('profile/',profile,name='profile'),
    path('blog/',include('blog.urls')),
    path('blogpost/<int:id>', blogpost , name='blogpost'),
    path('addpost/',AddPostView.as_view(), name='addpost'),
    path('blogpost/updatepost/<int:pk>' , UpdatePostView.as_view(), name = 'updatepost'),
    path('blogpost/<int:pk>/deletepost/' , DeletePostView.as_view(), name = 'deletepost'),
]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
