from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from home.models import Post, Comment


@login_required
def delete_post(self, request, id):

    if request.method == 'POST':
        post = Post.objects.get(id=id)
        if post.author == request.user.id:
            post.delete()
        else:
            raise PermissionDenied
    else:
        raise PermissionDenied
