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

        form_data = {
            'title': request.POST['title'],
            'category': request.POST['email'],
            'excerpt': request.POST['excerpt'],
            'content': request.POST['content'],
        }
        post_form = PostForm(form_data)

        if post_form.is_valid():

            user = User.objects.get(id=request.user.id)
            print(user)
            post_form.instance.author = request.user
            post = post_form.save(commit=False)
            post.save()

            messages.add_message(
                request, messages.SUCCESS,
                'Your post was successful!'
            )
            return render(
                                        request(
                                                '/'
                                        ))
        else:
            post_form = PostForm(data=post_form)
    else:
        post_form = PostForm()


def upload_post(request):

    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.instance.author = request.user
            form.save()
        else:
            form = PostForm()
    return render(request, '/create_post/create_post.html')