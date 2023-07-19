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
from django.template.defaultfilters import slugify
import random


@login_required
def create_post(request):

    if request.method == 'POST':

        # get the post.data into a PostForm
        post_form = PostForm(data=request.POST)

        # Check form valid
        if post_form.is_valid():

            # if it is, assign author and slug
            post_form.instance.author = request.user
            post_form.instance.slug = slugify(
                f'\
                {request.POST["title"]}-\
                {post_form.instance.author}-\
                {random.randint(0, 10000)}'
            )

        # Check if object with that slug already exists
        # if it doesent, save the post
        if len(Post.objects.filter(slug=post_form.instance.slug)) == 0:
            post = post_form.save(commit=False)
            post.save()
            messages.add_message(
                request, messages.SUCCESS,
                'Post was successful!'
            )
            return HttpResponseRedirect(
                reverse('post_detail', args=[post.slug])
            )
        # otherwise, "reload" create_post with message
        # + the data user entered
        else:
            data = {
                'title': request.POST['title'],
                'category': request.POST['category'],
                'excerpt': request.POST['excerpt'],
                'content': request.POST['content']
            }
            messages.add_message(
                request, messages.WARNING,
                'Something went wrong, please try again'
            )
            return render(
                request,
                "create_post/create_post.html",
                {
                    "post_form": PostForm(data=data)
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
