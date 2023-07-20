from django.test import TestCase, Client
from django.shortcuts import reverse
from django.contrib.auth.models import User
from home.models import Post, Comment, Category


class TestDeleteActions(TestCase):

    def setUp(self):

        # Set up superuser and login
        user = User.objects.create_superuser(
            username='superuser',
            password='secret',
            email='admin@example.com',
        )

        user_two = User.objects.create(
            username='test_user',
            password='test_secret',
            email='test@example.com'
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

        post_two = Post.objects.create(
            title='test2',
            author=user_two,
            content="test2",
            category=category,
        )
        post_two.save()

        comment = Comment.objects.create(
            author=user,
            body='test comment',
            post=post
        )
        comment.save()

        comment_two = Comment.objects.create(
            author=user_two,
            body='test comment by second user',
            post=post
        )
        comment_two.save()

        comment_three = Comment.objects.create(
            author=user,
            body='test comment on post_two',
            post=post
        )
        comment_two.save()

    # test to delete a post when user is post.author
    def test_delete_post_as_related_user(self):

        # get user and login
        user = User.objects.get(id=1)
        self.client.force_login(user=user)

        # get user object, post object with id=1 and set url
        post = Post.objects.get(id=1)

        # get all posts
        posts = Post.objects.all()

        # len() should return 2
        self.assertEqual(len(posts), 2)

        # call the post_delete view for post
        response = self.client.post(
            f'/delete_actions/delete_post/{post.id}/',
            follow=True
        )

        # get all posts
        posts = Post.objects.all()

        # assert there's only 1 post left in posts
        self.assertEqual(len(posts), 1)
        # and that the title corresponds to test2
        self.assertEqual(posts[0].title, 'test2')

        # assert status is ok and user redirects to /profile/
        self.assertEqual(response.status_code, 200)
        self.assertRedirects(response, '/profile/')

    def test_delete_post_as_not_related_user(self):

        # get user and login
        user = User.objects.get(id=1)
        self.client.force_login(user=user)

        # get all posts as well as the one created by user_two
        posts = Post.objects.all()
        post = Post.objects.get(id=2)

        # len() should return 2
        self.assertEqual(len(posts), 2)

        # call the post_delete view for post
        response = self.client.post(
            f'/delete_actions/delete_post/{post.id}/',
            follow=True
        )

        # should return 403: forbidden
        self.assertEqual(response.status_code, 403)

        # get all posts
        posts = Post.objects.all()

        # there should be 2 posts
        self.assertEqual(len(posts), 2)

    def test_delete_comment_as_related_user(self):

        user = User.objects.get(id=1)
        self.client.force_login(user=user)

        # get comments and comment from user
        comments = Comment.objects.all()
        comment = Comment.objects.get(id=1)

        # assert user owns the comment
        self.assertEqual(comment.author.username, user.username)

        # comments should contain 3 comments
        self.assertEqual(len(comments), 3)

        # call the comment_delete view for comment
        response = self.client.post(
            f'/delete_actions/delete_comment/{comment.id}/',
            follow=True
        )

        # assert status_code is ok
        self.assertEqual(response.status_code, 200)

        # get all remaining comments
        comments = Comment.objects.all()

        # assert only 2 comments left
        self.assertEqual(len(comments), 2)

        # try to filter out delete comment and assert len() is 0
        self.assertEqual(len(Comment.objects.filter(id=1)), 0)

        # assert redirects to profile
        self.assertRedirects(response, '/profile/')

    def test_delete_comment_as_not_related_user(self):

        user = User.objects.get(id=1)
        self.client.force_login(user=user)

        # get comments and comment from user_two
        comments = Comment.objects.all()
        comment = Comment.objects.get(id=2)

        # assert user is not comment.author
        self.assertFalse(comment.author is user)

        # comments should contain 3 comments
        self.assertEqual(len(comments), 3)

        # call the delete_comment view for selected comment
        response = self.client.post(
            f'/delete_actions/delete_comment/{comment.id}/',
            follow=True
        )

        # should return 403: forbidden
        self.assertEqual(response.status_code, 403)

        # get all comments
        comments = Comment.objects.all()
        self.assertEqual(len(comments), 3)