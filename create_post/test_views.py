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

        user = User.objects.get(id=1)

        response = self.client.get('/create_post/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(
            response, 'create_post/create_post.html', 'base.html'
        )
