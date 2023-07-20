from django.urls import path
from . import views

urlpatterns = [
    path(
        'delete_post/<int:id>/',
        views.delete_post,
        name='delete_post'
    ),
]
