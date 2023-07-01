from django.shortcuts import reverse
from django.test import TestCase
from django.contrib.auth.models import User
from home.models import Post, Category, Comment


class TestPostView(TestCase):

    '''
    Sourced from CI pp-4 masterclass
    '''
    def setUp(self):
        user = User.objects.create(username="test", password="test")
        post = Post.objects.create(
            title="Test post", author=user,
            excerpt="Test excerpt",
            content="Test content", status=1
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
        self.client.post(reverse('post_like', args=[post.slug]))
        post = Post.objects.filter(slug=post.slug).first()
        self.assertEqual(post.number_of_likes(), 1)

    def test_unlike(self):

        user = User.objects.get(id=1)
        post = Post.objects.get(id=1)

        self.client.force_login(user)

        # Likes post like in test above, the unlikes by calling the view again
        self.client.post(reverse('post_like', args=[post.slug]))
        self.client.post(reverse('post_like', args=[post.slug]))
        # Filters the post through slug
        post = Post.objects.filter(slug=post.slug).first()
        # Tests that number of likes is actually 0
        self.assertEqual(post.number_of_likes(), 0)

    def test_comment(self):
        '''
        This has been edited since i dont use the 'commented' boolean
        I put some redundancy in just to be safe
        '''

        user = User.objects.get(id=1)
        post = Post.objects.get(id=1)
        self.client.force_login(user)
        # Tests that post has no comments
        self.assertTrue(post.comments.count() == 0)
        # Mocks a comment posted by user @ post
        response = self.client.post(reverse('post_detail', args=[post.slug]), {
            'body': 'This is a test comment'
        })
        '''
        Re-check above statement but with False instead
        This is the redundancy mentioned above
        '''
        self.assertFalse(post.comments.count() == 0)
        self.assertEqual(len(response.context['comments']), 1)
        self.assertEqual(
            response.context['comments'][0].body, 'This is a test comment'
        )

    def test_liked_boolean(self):
        '''
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
        self.assertTrue(response.context['liked'] is False)

    def test_comment_form_is_passed(self):

        user = User.objects.get(id=1)
        post = Post.objects.get(id=1)
