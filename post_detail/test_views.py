from django.shortcuts import reverse
from django.test import TestCase
from django.contrib.auth.models import User
from home.models import Post, Category, Comment
from django.contrib.auth.models import AnonymousUser


class TestPostView(TestCase):

    '''
    Sourced from CI pp-4 masterclass
    '''
    def setUp(self):

        user = User.objects.create(username="test", password="test")
        post = Post.objects.create(
            title="Test post", author=user,
            excerpt="Test excerpt",
            content="Test content", status=1,
            slug='meow',
        )

        post.save()

    def test_get_post(self):

        # Get the post from setUp()
        post = Post.objects.get(id=1)

        response = self.client.get(reverse('post_detail', args=[post.slug]))

        # Tests statuscode is ok and correct template is used
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'post_detail/post_detail.html')

    def test_like(self):

        user = User.objects.get(id=1)
        post = Post.objects.get(id=1)

        self.client.force_login(user)
        post = Post.objects.filter(slug=post.slug).first()
        self.client.post(reverse('post_like', args=[post.slug]))
        self.assertEqual(post.number_of_likes(), 1)

    def test_unlike(self):

        user = User.objects.get(id=1)
        post = Post.objects.get(id=1)

        self.client.force_login(user)

        # Likes post like in test above, the unlikes by calling the view again
        self.client.post(reverse('post_like', args=[post.slug]))
        # Filters the post through slug
        post = Post.objects.filter(slug=post.slug).first()
        # Tests that number of likes is actually 0
        self.assertEqual(post.number_of_likes(), 1)
        # Unliking
        self.client.post(reverse('post_like', args=[post.slug]))
        self.assertEqual(post.number_of_likes(), 0)

    def test_comment(self):

        user = User.objects.get(id=1)
        post = Post.objects.get(id=1)
        self.client.force_login(user)
        # Tests that post has no comments
        self.assertTrue(post.comments.count() == 0)
        # Mocks a comment posted by user @ post
        response = self.client.post(reverse('post_detail', args=[post.slug]), {
            'author': user,
            'body': 'This is a test comment'
        })
        '''
        Re-check above statement but with False instead
        '''
        self.assertFalse(post.comments.count() == 0)
        self.assertEqual(len(response.context['comments']), 1)
        # assert the correct comment is in the dict
        self.assertEqual(
            response.context['comments'][0].body, 'This is a test comment'
        )

    def test_liked_boolean(self):
        '''
        Test if like view changes the liked boolean correctly
        '''
        user = User.objects.get(id=1)
        post = Post.objects.get(id=1)

        self.client.force_login(user)

        # Asserts liked boolean is False
        response = self.client.get(reverse('post_detail', args=[post.slug]))
        self.assertTrue(response.context['liked'] is False)

        # Likes the post, then checks if boolean is updated to True
        response = self.client.post(reverse('post_like', args=[post.slug]))
        response = self.client.get(reverse('post_detail', args=[post.slug]))
        self.assertTrue(response.context['liked'] is True)

    def test_comment_not_logged_in_redirects(self):

        user = AnonymousUser()
        post = Post.objects.get(id=1)

        response = self.client.post(reverse('post_detail', args=[post.slug]), {
            'author': user,
            'body': 'This is a test comment'
        })

        # assert status code is 302 and that anon_user is redirected to login
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, expected_url='/accounts/login/')
