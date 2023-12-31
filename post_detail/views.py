from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic
from django.contrib import messages
from django.http import HttpResponseRedirect
from home.models import Post, Comment
from .forms import CommentForm
from profiles.models import UserProfile
from django.core.exceptions import PermissionDenied


def post_detail(request, slug, *args, **kwargs):
    """
    Sourced from CodeInstitute
    """

    queryset = Post.objects.filter(status=1)
    post = get_object_or_404(queryset, slug=slug)
    comments = post.comments.filter(approved=True).order_by("-created_on")

    # set liked and commented to False for handling template rendering
    liked = False

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

                # If 'parent' is in post request
                if 'parent' in request.POST:
                    if post.author == request.user:
                        # Get the comment isntance corresponding to captured id
                        comment.parent = Comment.objects.get(
                            id=request.POST['parent']
                        )
                    else:
                        raise PermissionDenied
                # Save comment and return to post_detail
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
    post_obj = Post.objects.get(slug=slug)

    # check that the method is POST and user is not anon
    if request.method == "POST" and request.user.is_authenticated:
        # Get the users profile
        user_profile = UserProfile.objects.get(user=request.user)

        # If already liked
        if post.likes.filter(id=request.user.id).exists():
            # remove like from post
            post.likes.remove(request.user)
            # remove post from UserProfile.liked_posts
            user_profile.liked_posts.remove(post_obj)
        # If not, just add instead
        else:
            post.likes.add(request.user)
            user_profile.liked_posts.add(post_obj)

    return HttpResponseRedirect(reverse('post_detail', args=[slug]))
