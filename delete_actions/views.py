from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from home.models import Post, Comment
from django.shortcuts import HttpResponseRedirect, reverse


@login_required
def delete_post(request, id):

    template = '/profiles/profile.html'

    if request.method == 'POST':
        post = Post.objects.get(id=id)
        if post.author.id == request.user.id:
            post.delete()
        else:
            raise PermissionDenied
    return HttpResponseRedirect(reverse('profile'))