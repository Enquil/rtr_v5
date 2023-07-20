from django.urls import path
from . import views

urlpatterns = [
    path(
        'delete/<int:id>/',
        views.delete_post,
        name='delete_post'
    ),
]
