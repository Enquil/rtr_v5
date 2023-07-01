from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('create_post/', views.create_post, name='create_post'),
]
