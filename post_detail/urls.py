from django.urls import path
from . import views


urlpatterns = [
    path('<slug:slug>/', views.post_detail, name='post_detail'),
    path('like/<slug:slug>', views.post_like, name='post_like'),
]
