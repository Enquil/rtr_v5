from home.models import Post, Comment
from django.views import View
from django.shortcuts import (
    render, get_object_or_404,
    redirect, reverse
)
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from .models import UserProfile


class ProfileView(View):

    def get(self, request, *args, **kwargs):

        profile = get_object_or_404(UserProfile, user=request.user)
        posts = Post.objects.filter(author=profile.user.id)
        comments = Comment.objects.filter(author=profile.user.id)

        return render(
            request,
            "profiles/profile.html",
            {
                'profile': profile,
                'posts': posts,
                'comments': comments,
            },
        )
