# from django.shortcuts import render, get_object_or_404, reverse
# from create_post.forms import PostForm
# from home.models import Post, Category
# from django.contrib.auth.decorators import login_required
# from django.contrib import messages
# from django.core.exceptions import PermissionDenied
# from django.http import HttpResponseRedirect


# @login_required
# def edit_post(request, slug):
#     """
#     view to edit comments
#     Sourced From CodeInstitute
#     (Just a spin on the edit_comment view)
#     """

#     # If request.POST
#     if request.method == 'POST':
#         print(request.POST)
#         # gets posts with status = 1
#         queryset = Post.objects.filter(status=1)
#         # gets the post from queryset using slug as filter
#         post = queryset.filter(slug=slug).first()
#         # saves slug for redirect
#         slug = post.slug
#         # get post data in a variable
#         post_form = PostForm(data=request.POST, instance=post)
#         # if all fields are good:
#         if post_form.is_valid():
#             # Check if post.author matches user trying to edit the post
#             if post.author == request.user:
#                 # save post (false commit) and make post.author request.user
#                 post = post_form.save(commit=False)
#                 post.author = request.user
#                 # save post for real
#                 post.save()

#                 # Redirect to Post with a success message
#                 messages.add_message(
#                     request, messages.SUCCESS, 'Post Updated!'
#                 )
#                 return HttpResponseRedirect(
#                     reverse('post_detail', args=[slug])
#                 )
#             # If user doesent match post.author
#             else:
#                 raise PermissionDenied
#         # Should something be missing in the form:
#         else:
#             return render(
#                 request,
#                 "edit_post/edit_post.html",
#                 {
#                     "post_form": PostForm(instance=post)
#                 },
#             )

#     else:
#         queryset = Post.objects.filter(status=1)
#         post = get_object_or_404(queryset, slug=slug)

#         if post.author == request.user:

#             return render(
#                 request,
#                 "edit_post/edit_post.html",
#                 {
#                     "post_form": PostForm(instance=post)
#                 },
#             )
#         else:
#             raise PermissionDenied

from django.views.generic.edit import UpdateView
from django.contrib import messages
from django.urls import reverse
from home.models import Post
from create_post.forms import PostForm
from django.core.exceptions import PermissionDenied


class PostUpdate(UpdateView):
    model = Post
    fields = ['title', 'category', 'excerpt', 'content']
    template_name = 'edit_post/edit_post.html'
    success_url = f'/profile/'

    def get_object(self, queryset=None):
        obj = super(PostUpdate, self).get_object(queryset)
        if obj.author != self.request.user:
            raise PermissionDenied
        return obj

    def form_valid(self, form):
        print(form.data)
        messages.success(self.request, "The task was updated successfully.")
        return super(PostUpdate, self).form_valid(form)
