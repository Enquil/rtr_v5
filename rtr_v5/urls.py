"""rtr_v5 URL Configuration

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
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('', include('home.urls'), name='home_urls'),
    path('post_detail/', include('post_detail.urls'), name='post_detail_urls'),
    path(
        'create_post/',
        include('create_post.urls'),
        name='create_post_urls'
        ),
    path(
        'edit_post/',
        include('edit_post.urls'),
        name='edit_post_urls'),
    path(
        'profile/',
        include('profiles.urls'),
        name='profile_urls'
        ),
    path(
        'delete_actions/',
        include('delete_actions.urls'),
        name='delete_actions_urls'
        ),
]
