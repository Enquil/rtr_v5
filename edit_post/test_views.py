from django.test import TestCase
from home.models import Post, Comment, Category
from django.contrib.auth.models import User
from create_post.forms import PostForm
from django.shortcuts import render, get_object_or_404, reverse


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
            title='test',
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

        post = Post.objects.get(id=1)
        user2 = User.objects.get(id=2)
        self.client.force_login(user2)
        response = self.client.get(f'/edit_post/{post.slug}/')
        self.assertEqual(response.status_code, 403)

    def test_post_edit_post(self):
        post = Post.objects.get(id=1)
        user = User.objects.get(id=1)
        self.client.force_login(user)
        response = self.client.post(
            reverse('edit_post', kwargs={'slug': post.slug}),
            {'title': 'The Catcher in the Rye',
             'category': 'J.D. Salinger',
             'excerpt': 'new excerpt',
             'content': 'new content'}
        )

        self.assertEqual(response.status_code, 200)
        # self.assertRedirects()
        post.refresh_from_db()
        print(post)
        # self.assertEqual(post.content, 'new content')
