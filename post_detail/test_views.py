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
        comments = Comment.objects.filter(post=1)

        # There should be one comment in this list
        self.assertEqual(len(comments), 1)

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

    def test_comment_parent_as_author(self):

        # Login user and get their post
        user = User.objects.get(id=1)
        post = Post.objects.get(id=1)
        self.client.force_login(user)

        # Create comment from new user
        comment = Comment.objects.create(
            author=User.objects.create(
                username='test_user_two',
                password='meow'
            ),
            post=post,
            body='test comment',
            approved=True,
        )
        comment.save()

        # assert id and.is_top_level on comment for tests below
        self.assertEqual(comment.id, 1)
        self.assertTrue(comment.is_top_level)
        # assert it has no children
        self.assertEqual(len(comment.children), 0)

        response = self.client.post(reverse('post_detail', args=[post.slug]), {
            'author': user,
            'body': 'test parent comment',
            'parent': comment.id,
        })

        # should now = 1
        self.assertEqual(len(comment.children), 1)
        # should have the body of the comment created above
        self.assertEqual(comment.children[0].body, 'test parent comment')
        # Should not be a top level comment
        self.assertFalse(comment.children[0].is_top_level)

    def test_parent_comment_wrong_user(self):

        user = User.objects.get(id=1)
        post = Post.objects.get(id=1)

        user_two = User.objects.create(
            username='test_user_two',
            password='meow'
        )
        self.client.force_login(user_two)

        comment = Comment.objects.create(
            author=user_two,
            post=post,
            body='test comment',
            approved=True,
        )
        comment.save()

        # try to post a comment with parent = comment, on post by user
        response = self.client.post(reverse('post_detail', args=[post.slug]), {
            'author': user_two,
            'body': 'test parent comment',
            'parent': comment.id,
        })

        # should return 403 since user is the post owner
        self.assertEqual(response.status_code, 403)
