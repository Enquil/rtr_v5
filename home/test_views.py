from django.test import RequestFactory, TestCase
from django.views import View
from django.shortcuts import render
from django.contrib.auth.models import User
from .models import Category, Post
from django.contrib import messages
from django.shortcuts import (render, get_object_or_404,
                              redirect, reverse)
from django.http import (HttpResponse,
                         HttpResponseRedirect)


class TestPostList(TestCase):

    def setUp(self):

        user = User.objects.create(
            username='alan',
            is_superuser=True,
            password='enigma'
        )

        category = Category.objects.create(
            friendly_name='General',
        )

        category2 = Category.objects.create(
            friendly_name='Art and Entertainment',
        )

        post = Post.objects.create(
            title='how to crack codes',
            author=user,
            content="so easy",
            category=category,
        )

        post2 = Post.objects.create(
            title='Calculating machines',
            author=user,
            content="sometimes, 1 is 0",
            category=category2,
        )

    def test_get_post_list(self):

        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home/index.html', 'base.html')

    def test_filter_by_category(self):

        post = Post.objects.get(id=1)
        post2 = Post.objects.get(id=2)
        response = self.client.get('/')
