from django.shortcuts import reverse
from django.test import TestCase
from django.contrib.auth.models import User
from home.models import Post, Comment


class TestPostDelete(TestCase):

    def setUp(self):

        c = Client()

        user = User.objects.create(username="test", password="test")

        post = Post.objects.create(
            title="Test post", author=user,
            excerpt="Test excerpt",
            content="Test content", status=1,
            slug='meow',
        )