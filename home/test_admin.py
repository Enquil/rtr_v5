from .admin import PostAdmin, CommentAdmin
from django.test import TestCase, Client
from django.contrib.admin.sites import AdminSite
from home.models import Post, Comment, Category
from django.contrib.auth.models import User


class TestPostAdminActions(TestCase):

    def setUp(self):

        # Set up superuser and login
        user = User.objects.create_superuser(
            username='superuser', password='secret', email='admin@example.com'
        )
        c = Client()
        c.login(username='superuser', password='secret')

        category = Category.objects.create(
            friendly_name='test'
        )
        category.save()

        post = Post.objects.create(
            title='test',
            author=user,
            content="test",
            category=category,
        )
        post.save()

        post2 = Post.objects.create(
            title='test2',
            author=user,
            content="test2",
            category=category,
        )
        post2.save()

    def test_disable_posts(self):

        '''
        disable_post function test
        '''

        # get first post in a queryset to compare with post_two
        # post_two status should remain same throughout test
        posts = Post.objects.filter(id=1)

        self.assertEqual(Post.objects.get(id=1).status, 1)
        self.assertEqual(Post.objects.get(id=2).status, 1)

        # call the admin function to disable posts
        PostAdmin.disable_selected_posts(
            self,
            'admin:home_post_change',
            posts
        )

        # get all posts
        posts = Post.objects.all()
        # Refresh the whole queryset from database
        [p.refresh_from_db() for p in posts]

        # should return 2
        self.assertEqual(Post.objects.get(id=1).status, 2)
        self.assertEqual(Post.objects.get(id=2).status, 1)

    def test_publish_posts(self):
        '''
        Disable post test
        first 20 lines is the test above
        '''
        # get first post in a queryset to compare with post_two
        # post_two status should remain same throughout test
        posts = Post.objects.filter(id=1)

        self.assertEqual(Post.objects.get(id=1).status, 1)
        self.assertEqual(Post.objects.get(id=2).status, 1)

        # call the admin function to disable posts
        PostAdmin.disable_selected_posts(
            self,
            'admin:home_post_change',
            posts
        )

        # get all posts
        posts = Post.objects.all()

        # Refresh the whole queryset from database
        [p.refresh_from_db() for p in posts]

        # only post 1 should return status=2
        self.assertEqual(Post.objects.get(id=1).status, 2)
        self.assertEqual(Post.objects.get(id=2).status, 1)

        # call the admin function to disable posts
        PostAdmin.publish_selected_posts(
            self,
            'admin:home_post_change',
            posts
        )

        # Refresh from db again
        [p.refresh_from_db() for p in posts]

        # Should return both posts as status=1
        self.assertEqual(Post.objects.get(id=1).status, 1)
        self.assertEqual(Post.objects.get(id=2).status, 1)


class TestCommentAdmin(TestCase):

    def setUp(self):

        # Set up superuser and login
        user = User.objects.create_superuser(
            username='superuser',
            password='secret',
            email='admin@example.com'
        )

        c = Client()

        c.login(
            username='superuser',
            password='secret'
        )

        category = Category.objects.create(
            friendly_name='test'
        )
        category.save()

        post = Post.objects.create(
            title='test',
            author=user,
            content="test",
            category=category,
        )
        post.save()

        comment = Comment.objects.create(
            author=user,
            post=post,
            body='test',
            approved=True
        )
        comment.save()

        comment_two = Comment.objects.create(
            author=user,
            post=post,
            body='test',
            approved=True
        )
        comment_two.save()

    def test_disable_comments(self):

        # get first comment as queryset
        comments = Comment.objects.filter(approved=True)

        self.assertTrue(Comment.objects.get(id=1).approved)
        self.assertTrue(Comment.objects.get(id=2).approved)

        CommentAdmin.disable_selected_comments(
            self,
            'admin:home_comment_change',
            comments
        )

        # check approved is false for comment 1 and not comment 2
        self.assertFalse(Comment.objects.get(id=1).approved)
        self.assertFalse(Comment.objects.get(id=2).approved)

    def test_approve_comments(self):

        comments = Comment.objects.filter(id=1)

        self.assertTrue(Comment.objects.get(id=1).approved)
        self.assertTrue(Comment.objects.get(id=2).approved)

        CommentAdmin.disable_selected_comments(
            self,
            'admin:home_comment_change',
            comments
        )

        # Refresh from db
        [c.refresh_from_db() for c in comments]

        # approved should return false for comment with id 1
        self.assertFalse(Comment.objects.get(id=1).approved)
        self.assertTrue(Comment.objects.get(id=2).approved)

        CommentAdmin.approve_selected_comments(
            self,
            'admin:home_comment_change',
            comments
        )

        # Refresh from db
        [c.refresh_from_db() for c in comments]

        # both comments should return True for comment.approved
        self.assertTrue(Comment.objects.get(id=1).approved)
        self.assertTrue(Comment.objects.get(id=2).approved)
