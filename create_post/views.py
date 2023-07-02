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


@login_required
def create_post(request):

    if request.method == 'POST':
        post_form = PostForm(data=request.POST)
        if post_form.is_valid():
            post_form.instance.author = request.user
            post = post_form.save(commit=False)
            post.save()
        else:
            form = PostForm()

        '''
        if form is valid and user is logged in
        add success message and redirect to the created post
        '''
        messages.add_message(
                request, messages.SUCCESS,
                'Post was successful!'
            )
        return HttpResponseRedirect(
            reverse('post_detail', args=[post.slug])
        )
    else:
        return render(
            request,
            "create_post/create_post.html",
            {
                "post_form": PostForm()
            },
        )
