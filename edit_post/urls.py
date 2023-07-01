from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required


urlpatterns = [
    path('<slug:slug>/', views.edit_post, name='edit_post'),
]