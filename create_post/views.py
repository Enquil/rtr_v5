from django.views import View
from django.shortcuts import render
from home.models import Post
from django.contrib.auth.models import User
from .forms import PostForm
from django.contrib import messages
from django.shortcuts import (render, get_object_or_404,
                              redirect, reverse)
from django.http import (HttpResponse,
                         HttpResponseRedirect)
from django.contrib.auth.decorators import login_required


def create_post(request):

    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.instance.author = request.user
            form.save()
        else:
            form = PostForm(data=form)
        return render(
            request,
            "create_post/create_post.html",
            {
                "post_form": PostForm()
            },
        )
    else:
        return render(
            request,
            "create_post/create_post.html",
            {
                "post_form": PostForm()
            },
        )


# def upload_post(request):

#     if request.method == 'POST':
#         form = PostForm(request.POST)
#         if form.is_valid():
#             form.instance.author = request.user
#             form.save()
#         else:
#             form = PostForm(data=form)
#     return HttpResponseRedirect(reverse('/'))
