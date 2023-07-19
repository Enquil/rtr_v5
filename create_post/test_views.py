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

    def test_post_create_post_user(self):

        user = User.objects.get(id=1)
        self.client.force_login(user)

        post_data = {
             'title': 'new title 1234',
             'author': user,
             'excerpt': 'new excerpt',
             'content': 'new content',
             'category': 1,
             'created_on': datetime.now(),
             'status': 1,
        }

        response = self.client.get('/create_post/')

        # First get all posts and make sure there's none
        posts = Post.objects.all()
        self.assertEqual(len(posts), 0)

        # send a post request, it should then redirect to the post_detail view
        response = self.client.post(reverse('create_post'), data=post_data)

        # status_code should be 302
        self.assertEqual(response.status_code, 302)
        # expected url is: /post_detail/ + the post.slug
        self.assertRedirects(
            response, expected_url='/post_detail/new-title-1234-alan1/'
        )

        # gets all posts again, (if any exists)
        posts = Post.objects.all()
        # Should return one if post.method was successful on view
        self.assertEqual(len(posts), 1)
        # Finally, let's see if that post matches the data we posted
        self.assertAlmostEqual(posts[0].title, 'new title 1234')

    def test_title_user_already_exists(self):

        user = User.objects.get(id=1)
        self.client.force_login(user)

        post = Post.objects.create(
            title="test",
            author=user,
            excerpt="test",
            content="test", status=1,
            slug='test-alan1',
        )
        post.save()

        post_data = {
             'title': 'test',
             'author': user,
             'excerpt': 'test',
             'content': 'test',
             'category': 1,
             'created_on': datetime.now(),
             'status': 1,
        }

        # get the create_post view and assert there is a saved post.model
        response = self.client.get('/create_post/')
        self.assertEqual(len(Post.objects.all()), 1)

        # post the data and make sure a message is stored in context
        response = self.client.post(reverse('create_post'), data=post_data)
        messages = list([response.context['messages']])
        self.assertEqual(len(messages), 1)
        # check that message is the one set in create_post.view
        self.assertEqual(
            [m.message for m in list(response.context['messages'])],
            ['You already have a post named that, select another title']
        )
