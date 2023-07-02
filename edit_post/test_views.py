from django.test import TestCase
from home.models import Post, Comment, Category
from django.contrib.auth.models import User
from create_post.forms import PostForm
from django.shortcuts import render, get_object_or_404, reverse
from datetime import datetime
from django.utils.text import slugify
from .views import PostUpdate


class EditPostViewTest(TestCase):
    '''
    Test class for View: create_post
    '''
    def setUp(self):

        category = Category.objects.create(
            friendly_name='General'
        )

        category2 = Category.objects.create(
            friendly_name='Art and Entertainment'
        )

        user = User.objects.create(
            username='alan',
            is_superuser=True,
            password='enigma'
        )

        user2 = User.objects.create(
            username='ada',
            is_superuser=True,
            password='enigma'
        )

        post = Post.objects.create(
            title='new',
            category=category,
            author=user,
            content='test'
        )

        post2 = Post.objects.create(
            title='test2',
            category=category,
            author=user2,
            status=0
        )

    def test_get_edit_post_user_logged_in(self):
        '''
        Test access to edit_post with logged in user
        '''
        # force login with user object and assign Post.object
        post = Post.objects.get(id=1)
        user = User.objects.get(id=1)
        self.client.force_login(user)

        response = self.client.get(f'/edit_post/{post.slug}/')
        # Test if response.status_code is ok
        self.assertEqual(response.status_code, 200)
        # Test if correct template is being used
        self.assertTemplateUsed(
            response, 'edit_post/edit_post.html', 'base.html'
        )

    def test_get_edit_post_user_anonymous(self):
        '''
        Test access to edit_post when not logged in
        '''
        post = Post.objects.get(id=1)
        response = self.client.get(f'/edit_post/{post.slug}/')

        self.assertEqual(response.status_code, 302)
        self.assertRedirects(
            response,
            expected_url=f'/accounts/login/?next=/edit_post/{post.slug}/'
        )

    def test_get_edit_post_wrong_user(self):
        '''
        Test for when trying to edit another users post
        Logs in user2 and tries to access post with author: user
        '''
        post = Post.objects.get(id=1)
        user2 = User.objects.get(id=2)
        self.client.force_login(user2)

        # gets edit_post view with the post
        response = self.client.get(f'/edit_post/{post.slug}/')
        # should return 403: forbidden
        self.assertEqual(response.status_code, 403)

    def test_post_edit_post(self):
        # creates a mock category
        category = Category.objects.create(
            friendly_name='Ships and Giggles'
        )
        user = User.objects.get(id=1)
        self.client.force_login(user)

        # new form data to be sent with post request
        data = {
             'title': 'new title 1234',
             'author': user,
             'excerpt': 'new excerpt',
             'content': 'new content',
             'category': 3,
             'created_on': datetime.now(),
             'status': 1,
        }
        self.client.force_login(user)
        post = Post.objects.get(
            id=1
        )

        # sends a post request to /edit_post/post.slug/
        response = self.client.post(
            reverse('edit_post', kwargs={'slug': post.slug}), data
        )
        # Should return a 302 statuscode
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, expected_url='/profile/')
        # refreshes the post model from database
        post.refresh_from_db()
        self.assertEqual(post.excerpt, 'new excerpt')
        self.assertEqual(post.title, 'new title 1234')
        self.assertEqual(post.category.name, 'ships_giggles')

        # Just doublecheck to see that it's using the correct post
        # For good measure
        self.assertEqual(post.id, 1)
