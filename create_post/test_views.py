from django.test import TestCase
from home.models import Post, Comment, Category
from django.contrib.auth.models import User
from django.urls import reverse
from .forms import PostForm
from datetime import datetime


class CreatePostViewTest(TestCase):
    '''
    Test class for View: create_post
    '''
    def setUp(self):

        category = Category.objects.create(
            friendly_name='Art and Entertainment'
        )

        user = User.objects.create(
            username='alan',
            is_superuser=True,
            password='enigma'
        )

    def test_get_create_post_user_logged_in(self):
        '''
        Test access to create_post with logged in user
        '''
        # force login with user object
        user = User.objects.get(id=1)
        self.client.force_login(user)

        response = self.client.get('/create_post/')
        # Test if response.status_code is ok
        self.assertEqual(response.status_code, 200)
        # Test if correct template is being used
        self.assertTemplateUsed(
            response, 'create_post/create_post.html', 'base.html'
        )

    def test_get_create_post_user_anonymous(self):
        '''
        Test access to create_post when not logged in
        '''
        response = self.client.get('/create_post/')

        self.assertEqual(response.status_code, 302)
        self.assertRedirects(
            response, expected_url='/accounts/login/?next=/create_post/'
        )

    # def test_post_create_post_user(self):

    #     user = User.objects.get(id=1)
    #     self.client.force_login(user)

    #     data = {
    #          'title': 'new title 1234',
    #          'author': user,
    #          'excerpt': 'new excerpt',
    #          'content': 'new content',
    #          'category': 1,
    #          'created_on': datetime.now(),
    #          'status': 1,
    #     }
    #     # post_form = PostForm(instance=data)
    #     response = self.client.get('/create_post/')

    #     response = self.client.post('create_post', data)
    #     print(response.form.error)
    #     obj = Post.objects.all()
    #     print(len(post.objects.all()))
