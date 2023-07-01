from django.shortcuts import render

# Create your views here.


def create_post(request, *args, **kwargs):

    return render(
        request,
        "create_post/create_post.html",
        {
            "post_form": PostForm()
        },
    )

    if request.method == 'POST':

        post_form = PostForm(request.POST, request.FILES)
        if post_form.is_valid():

            user = User.objects.get(id=request.user.id)
            post_form.instance.author = request.user
            post = post_form.save(commit=False)
            post.save()

            messages.success(request, f'Post was successful!')
            return HttpResponseRedirect(
                                        reverse(
                                                'post_detail',
                                                args=[post.slug]
                                        ))
        else:
            post_form = PostForm()
