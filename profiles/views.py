from home.models import Post, Comment
from django.views import View
from django.shortcuts import (
    render, get_object_or_404,
    redirect, reverse
)
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from .models import UserProfile


def profile_view(request):

    profile = get_object_or_404(UserProfile, id=request.user.id)

    posts = Post.objects.filter(
        author=profile.user.id
    ).order_by('-created_on')

    comments = Comment.objects.filter(
        author=request.user.id
    ).order_by('-created_on')

    liked_posts = profile.liked_posts.all()

    return render(
        request,
        "profiles/profile.html",
        {
            'profile': profile,
            'posts': posts,
            'comments': comments,
            'liked_posts': liked_posts,
        },
    )
