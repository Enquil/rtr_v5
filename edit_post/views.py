from django.shortcuts import render, get_object_or_404, reverse
from create_post.forms import PostForm
from home.models import Post, Category
from django.contrib.auth.decorators import login_required


@login_required
def edit_post(request, slug):
    """
    view to edit comments
    """
    if request.method == 'POST':
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

# from django.views import View
# from django.shortcuts import render
# from home.models import Post
# from django.contrib.auth.models import User
# from django.contrib import messages
# from django.shortcuts import (render, get_object_or_404,
#                               redirect, reverse)
# from django.http import (HttpResponse,
#                          HttpResponseRedirect)
# from create_post.forms import PostForm
# from django.views.generic import UpdateView
# from django.http import Http404
# from django.core.exceptions import PermissionDenied


# class EditPost(UpdateView):

#     model = Post
#     form_class = PostForm
#     template_name = "edit_post/edit_post.html"
#     success_url = "/profile/"

#     def get_object(self, *args, **kwargs):
#         post = super(EditPost, self).get_object(*args, **kwargs)
#         if not post.author == self.request.user:
#             raise PermissionDenied
#         return post

#     def form_valid(self, form):
#         # This method is called when valid form data has been POSTed.
#         # It should return an HttpResponse.
#         return super().form_valid(form)