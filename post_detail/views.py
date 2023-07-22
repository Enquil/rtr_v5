from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic
from django.contrib import messages
from django.http import HttpResponseRedirect
from home.models import Post
from .forms import CommentForm


def post_detail(request, slug, *args, **kwargs):
    """
    Sourced from CodeInstitute
    """

    queryset = Post.objects.filter(status=1)
    post = get_object_or_404(queryset, slug=slug)
    comments = post.comments.filter(approved=True).order_by("-created_on")
    comment_count = len(comments)

    # set liked and commented to False for handling template rendering
    liked = False
    commented = False

    # check if user exists in post.likes and set liked to True if so
    if post.likes.filter(id=request.user.id).exists():
        liked = True

    # Comment Handling
    if request.method == "POST":

        # Redirect to login if trying to comment while not logged in
        if not request.user.is_authenticated:
            return HttpResponseRedirect(reverse('account_login'))
        # if logged in
        else:
            comment_form = CommentForm(data=request.POST)
            # Check validity of form
            if comment_form.is_valid():

                comment_form.instance.email = request.user.email
                comment_form.instance.author = request.user
                comment = comment_form.save(commit=False)
                comment.post = post
                comment.save()
                messages.add_message(
                    request, messages.SUCCESS,
                    'Your comment has been posted!'
                )
                return HttpResponseRedirect(
                    reverse('post_detail',
                            args=[slug])
                )
    # If not post-request
    else:
        comment_form = CommentForm()

    return render(
        request,
        'post_detail/post_detail.html',
        {
            "post": post,
            "comments": comments,
            "comment_count": comment_count,
            "liked": liked,
            "comment_form": comment_form
        },
    )


def post_like(request, slug, *args, **kwargs):
    """
    The view to update the likes. Although it should always be
    called using the POST method, we have still added some
    defensive programming to make sure.
    """
    post = get_object_or_404(Post, slug=slug)

    if request.method == "POST" and request.user.is_authenticated:
        if post.likes.filter(id=request.user.id).exists():
            post.likes.remove(request.user)
        else:
            post.likes.add(request.user)

    return HttpResponseRedirect(reverse('post_detail', args=[slug]))
