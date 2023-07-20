from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from home.models import Post, Comment
from django.shortcuts import HttpResponseRedirect, reverse
from django.contrib import messages


@login_required
def delete_post(request, id):

    if request.method == 'POST':

        # get post corresponding to id in request.POST and title
        post = Post.objects.get(id=id)
        title = post.title

        # if user is post-owner, delete it
        if post.author.id == request.user.id:

            post.delete()

            # return message to confirm deletion
            messages.add_message(
                request, messages.SUCCESS,
                f'Successfully deleted {post.title}'
            )
            # return to profile
            return HttpResponseRedirect(reverse('profile'))
        # if not
        else:
            raise PermissionDenied


@login_required
def delete_comment(request, id):

    if request.method == 'POST':

        # get comment corresponding to id in request.POST
        comment = Comment.objects.get(id=id)

        # if user is comment-owner, delete it
        if comment.author.id == request.user.id:

            comment.delete()

            # return message to confirm deletion
            messages.add_message(
                request, messages.SUCCESS,
                f'Successfully deleted comment'
            )
            # return to profile
            return HttpResponseRedirect(reverse('profile'))
        # if not
        else:
            raise PermissionDenied
