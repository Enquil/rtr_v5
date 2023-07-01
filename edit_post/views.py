from django.shortcuts import render, get_object_or_404, reverse
from create_post.forms import PostForm
from home.models import Post, Category
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.exceptions import PermissionDenied
from django.http import HttpResponseRedirect

@login_required
def edit_post(request, slug):
    """
    view to edit comments
    Sourced From CodeInstitute
    (Just a spin on the edit_comment view)
    """

    # If request.POST
    if request.method == 'POST':

        # gets posts with status = 1
        queryset = Post.objects.filter(status=1)
        # gets the post from queryset using slug as filter
        post = queryset.filter(slug=slug).first()
        # saves slug for redirect
        slug = post.slug
        # get post data in a variable
        post_form = PostForm(data=request.POST, instance=post)

        # if all fields are good:
        if post_form.is_valid():
            # Check if post.author matches user trying to edit the post
            if post.author == request.user:
                post = post_form.save(commit=False)
                post.author = request.user
                post.save()
                messages.add_message(request, messages.SUCCESS, 'Post Updated!')
                return HttpResponseRedirect(reverse('post_detail', args=[slug]))
            # If user doesent match post.author
            else:
                raise PermissionDenied
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
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)

        if post.author == request.user:

            return render(
                request,
                "create_post/create_post.html",
                {
                    "post_form": PostForm(instance=post)
                },
            )
        else:
            raise PermissionDenied
