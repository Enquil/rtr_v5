from django.test import TestCase
from home.models import Post, Comment, Category
from django.contrib.auth.models import User


class CreatePostViewTest(TestCase):
    '''
    Test class for View: create_post
    '''
    def setUp(self):

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
