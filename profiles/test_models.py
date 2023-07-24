from django.contrib.auth.models import User
from .models import UserProfile
from django.test import TestCase


class TestUserProfileModel(TestCase):
    '''
        Sourced from CI pp-4 masterclass
    '''
    def setUp(self):

        user = User.objects.create(
            username="test_user",
            password="test"
        )
        user.save()

    def test_str_method(self):

        user = User.objects.get(id=1)

        # Get user profile
        user_profile = UserProfile.objects.get(id=1)

        # call str method and assert str() method matches the username of user
        test_str = str(user_profile)
        self.assertEqual(test_str, user.username)
