from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required
from django.conf.urls import url

urlpatterns = [
    path('', views.create_post, name='create_post'),
]
