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


def create_post(request):

    return render(
        request,
        "create_post/create_post.html",
        {
            "post_form": PostForm()
        },
    )

    if request.method == 'POST':

        post_form = PostForm(data=request.POST)
        print(post_form)
        if post_form.is_valid():

            user = User.objects.get(id=request.user.id)
            post_form.instance.author = request.user
            post = post_form.save(commit=False)
            post.save()

            messages.add_message(
                request, messages.SUCCESS,
                'Your post was successful!'
            )
            return HttpResponseRedirect(
                                        reverse(
                                                'post_detail',
                                                args=[post.slug]
                                        ))
        else:
            post_form = PostForm(data=post_form)
    else:
        post_form = PostForm()
