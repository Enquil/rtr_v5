from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from home.models import Post, Comment
from django.shortcuts import HttpResponseRedirect, reverse
from django.contrib import messages


@login_required
def delete_post(request, id):

    # if user tries to access function through url
    if request.method == 'GET':
        raise PermissionDenied

    if request.method == 'POST':

        # get post corresponding to id in request.POST
        post = Post.objects.get(id=id)
        # if user is post owner, delete it
        if post.author.id == request.user.id:

            post.delete()

            # return message to confirm deletion
            messages.add_message(
                request, messages.SUCCESS,
                f'Successfully deleted post'
            )
            # return to profile
            return HttpResponseRedirect(reverse('profile'))

        # if not users post
        # this should not be callable
        # but just in case someone really fiddles with the page
        else:
            raise PermissionDenied


@login_required
def delete_comment(request, id):

    comment = Comment.objects.get(id=id)
    if request.method == 'GET' or comment.id != request.user.id:
        raise PermissionDenied

    else:
        # get comment corresponding to id in request.POST
        comment = Comment.objects.get(id=id)
        # if user is comment owner, delete it
        if comment.author.id == request.user.id:

            comment.delete()

            # return message to confirm deletion
            messages.add_message(
                request, messages.SUCCESS,
                f'Successfully deleted comment'
            )
            # return to profile
            return HttpResponseRedirect(reverse('profile'))
