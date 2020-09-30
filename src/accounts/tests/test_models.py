from django.test import TestCase
from django.contrib.auth import get_user_model

User = get_user_model()


class ModelTest(TestCase):

    def test_create_user_with_email_successfull(self):
        """
            Test Creating a new user
         """

        email = "root@root.com"
        password = 'pass@123'
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        """ Test the email for a new user"""
        email = "test@test.com"
        user = get_user_model().objects.create_user(email, 'test123')
        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):
        """ Test creating user email validations """

        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, 'test123')

    def test_create_new_superuser(self):
        """ Test creating new Superuser """
        user = User.objects.create_superuser('test3@gmail.com', 'test@123')

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
