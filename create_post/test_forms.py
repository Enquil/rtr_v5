from django.test import TestCase
from .forms import PostForm
from home.models import Post, Comment, Category
from django.contrib.auth.models import User


class TestPostForm(TestCase):
    '''
    Sourced From CodeInstitute
    Tests the PostForm
    '''
    def setUp(self):

        user = User.objects.create(
            username='alan',
            is_superuser=True,
            password='enigma'
        )

        category = Category.objects.create(
            friendly_name='General',
        )

    def test_category_field_required(self):
        '''
        Test if category is required in form
        '''
        user = User.objects.get(id=1)
        category = Category.objects.get(id=1)

        form = PostForm({'author': user, 'title': 'test',
                         'category': '',  'content': 'test'}
                        )

        # Test if form is valid, should return False
        self.assertFalse(form.is_valid())
        # Tests if 'category' is in form.errors.keys()
        self.assertIn('category', form.errors.keys())
        # Test if form error returns correct string
        self.assertEqual(form.errors['category'][0], 'This field is required.')
        # Tests if other required fields are okay
        self.assertFalse('title' in form.errors.keys())
        self.assertFalse('content' in form.errors.keys())

    def test_title_field_required(self):
        '''
        Test if title is required in form
        '''
        user = User.objects.get(id=1)
        category = Category.objects.get(id=1)

        form = PostForm({'author': user, 'title': 'test',
                         'category': category,  'content': ''}
                        )

        # Test if form is valid, should return False
        self.assertFalse(form.is_valid())
        # Tests if 'content' is in form.errors.keys()
        self.assertIn('content', form.errors.keys())
        # Test if form error returns correct string
        self.assertEqual(form.errors['content'][0], 'This field is required.')
        # Tests if other required fields are okay
        self.assertFalse('title' in form.errors.keys())
        self.assertFalse('category' in form.errors.keys())
