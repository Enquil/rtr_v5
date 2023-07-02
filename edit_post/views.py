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
    success_url = '/profile/'

    def get_object(self, queryset=None):
        obj = super(PostUpdate, self).get_object(queryset)
        if obj.author != self.request.user:
            raise PermissionDenied
        return obj

    def form_valid(self, form):
        messages.success(self.request, "The task was updated successfully.")
        return super(PostUpdate, self).form_valid(form)
