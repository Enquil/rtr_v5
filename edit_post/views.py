from django.views.generic.edit import UpdateView
from django.contrib import messages
from django.urls import reverse
from home.models import Post
from create_post.forms import PostForm
from django.core.exceptions import PermissionDenied


class PostUpdate(UpdateView):
    '''
    Basic Django Update View
    '''

    # Set what model to perform updates on and fields on relevant form
    model = Post
    fields = ['title', 'category', 'excerpt', 'content']

    # set template and redirection url
    template_name = 'edit_post/edit_post.html'
    success_url = '/profile/'

    # gets the selected post
    def get_object(self, queryset=None):
        obj = super(PostUpdate, self).get_object(queryset)

        # if user tries to access a post they didnt create
        if obj.author != self.request.user:
            raise PermissionDenied
        return obj

    # if form is valid, set a message and redirects to success_url
    def form_valid(self, form):
        messages.success(
            self.request,
            "The task was updated successfully."
        )
        return super(PostUpdate, self).form_valid(form)
